import numpy as np
from PIL import Image
from scipy.fftpack import dct as dct2d, idct as idct2d
from skimage.metrics import structural_similarity


def load_pic(file_path, mode='RGB'):
    try:
        pic = Image.open(file_path)
    except Exception as err:
        raise FileNotFoundError(f"Не удалось открыть изображение: {err}")
    return np.array(pic.convert(mode))


def write_pic(img_array, destination):
    img = Image.fromarray(img_array)
    img.save(destination)


def scramble_img(wm, rounds=1):
    side = wm.shape[0]
    if wm.shape[1] != side:
        raise ValueError("Для Арнольда нужно квадратное изображение.")
    T = np.array([[1, 1], [1, 2]])
    X, Y = np.meshgrid(np.arange(side), np.arange(side))
    flat = np.vstack((X.flatten(), Y.flatten()))
    for _ in range(rounds):
        flat = T @ flat % side
    output = np.zeros_like(wm)
    output[flat[1], flat[0]] = wm[Y.flatten(), X.flatten()]
    return output


def descramble_img(wm, rounds=1):
    side = wm.shape[0]
    if wm.shape[1] != side:
        raise ValueError("Для обратного Арнольда нужно квадратное изображение.")
    T_inv = np.array([[2, -1], [-1, 1]])
    X, Y = np.meshgrid(np.arange(side), np.arange(side))
    flat = np.vstack((X.flatten(), Y.flatten()))
    for _ in range(rounds):
        flat = T_inv @ flat % side
    restored = np.zeros_like(wm)
    restored[flat[1], flat[0]] = wm[Y.flatten(), X.flatten()]
    return restored


def split_dct(ch):
    h, w = ch.shape
    bh, bw = h // 8, w // 8
    segments = np.zeros((bh, bw, 8, 8), dtype=float)
    for y in range(bh):
        for x in range(bw):
            b = ch[y*8:(y+1)*8, x*8:(x+1)*8]
            segments[y, x] = dct2d(dct2d(b.T, norm='ortho').T, norm='ortho')
    return segments


def merge_idct(segments):
    bh, bw, _, _ = segments.shape
    restored = np.zeros((bh * 8, bw * 8), dtype=float)
    for y in range(bh):
        for x in range(bw):
            b = segments[y, x]
            restored[y*8:(y+1)*8, x*8:(x+1)*8] = idct2d(idct2d(b.T, norm='ortho').T, norm='ortho')
    return restored


def evaluate_diff(im1, im2):
    im1, im2 = im1.astype(np.float64), im2.astype(np.float64)
    mse_val = np.mean((im1 - im2) ** 2)
    psnr = 20 * np.log10(255.0 / np.sqrt(mse_val)) if mse_val else float('inf')
    try:
        ssim = structural_similarity(im1, im2, data_range=255, channel_axis=-1)
    except TypeError:
        ssim = structural_similarity(im1, im2, multichannel=True)
    return {'psnr': psnr, 'mse': mse_val, 'ssim': ssim}


def inject_wm(host_img, wm_bits, color_ch=0, rounds=1, p_val=1.0, q_val=1.0, weight=1.0):
    host = host_img.copy().astype(float)
    h, w, _ = host.shape
    h8, w8 = h - h % 8, w - w % 8
    if h != h8 or w != w8:
        host = host[:h8, :w8, :]
    trimmed = host_img[:host.shape[0], :host.shape[1], :].copy()

    ch_data = host[:, :, color_ch] - 128.0
    blocks = split_dct(ch_data)
    bh, bw, _, _ = blocks.shape

    wm_scrambled = scramble_img(wm_bits, rounds)
    flat_bits = wm_scrambled.flatten()
    bit_count = flat_bits.size

    max_capacity = (bh - 1) * bw if bh > 1 else 0
    if bit_count > max_capacity:
        raise ValueError(f"Недостаточная вместимость ({max_capacity}) для ЦВЗ размером {wm_bits.shape[0]}x{wm_bits.shape[1]}.")

    pi, qi, k = 3, 3, 0
    for y in range(1, bh):
        for x in range(bw):
            if k >= bit_count:
                break
            bit = flat_bits[k]
            base = blocks[y, x, 0, 0]
            alpha = np.sqrt(weight * abs(base)) if base != 0 else np.sqrt(weight)
            Ci = blocks[y, x, pi, qi]
            Cj = blocks[y-1, x, pi, qi]
            diff = Ci - Cj
            if bit == 1:
                while diff < q_val:
                    Ci += alpha
                    diff = Ci - Cj
            else:
                while diff > -p_val:
                    Ci -= alpha
                    diff = Ci - Cj
            blocks[y, x, pi, qi] = Ci
            k += 1
        if k >= bit_count:
            break

    updated = merge_idct(blocks) + 128.0
    updated = np.clip(np.round(updated), 0, 255).astype(np.uint8)
    result = trimmed.copy()
    result[:, :, color_ch] = updated
    stats = evaluate_diff(trimmed, result)
    fill_ratio = bit_count / max_capacity if max_capacity else 0.0
    return result, max_capacity, fill_ratio, stats


def retrieve_wm(embedded_img, wm_dim, color_ch=0, rounds=1):
    h, w, _ = embedded_img.shape
    h8, w8 = h - h % 8, w - w % 8
    ch = embedded_img[:h8, :w8, color_ch].astype(float) - 128.0
    blocks = split_dct(ch)

    N = wm_dim
    needed = N * N
    bh = h8 // 8
    bw = w8 // 8
    capacity = (bh - 1) * bw if bh > 1 else 0
    if needed > capacity:
        raise ValueError(f"Недостаточно данных ({capacity}) для восстановления ЦВЗ из {needed} бит.")
    bits = []
    pi, qi = 3, 3
    counter = 0
    for y in range(1, bh):
        for x in range(bw):
            if counter >= needed:
                break
            d = blocks[y, x, pi, qi] - blocks[y-1, x, pi, qi]
            bits.append(1 if d >= 0 else 0)
            counter += 1
        if counter >= needed:
            break
    if len(bits) < needed:
        raise ValueError(f"Извлечено {len(bits)} бит, ожидалось {needed}.")
    bit_array = np.array(bits, dtype=np.uint8).reshape((N, N))
    return descramble_img(bit_array, rounds)


def cli():
    while True:
        print("1. Встраивание ЦВЗ\n2. Извлечение ЦВЗ\n3. Выход")
        cmd = input(">: ").strip()
        if cmd == '1':
            container_path = input("Контейнер изображение: ").strip()
            try:
                host = load_pic(container_path)
            except Exception as err:
                print(f"Ошибка: {err}")
                continue

            wm_path = input("Изображение ЦВЗ (32x32 или 64x64): ").strip()
            try:
                wm_img = load_pic(wm_path, mode='L')
            except Exception as err:
                print(f"Ошибка: {err}")
                continue
            if wm_img.ndim != 2:
                print("ЦВЗ должно быть чёрно-белым.")
                continue
            if wm_img.shape[0] != wm_img.shape[1] or wm_img.shape[0] not in (32, 64):
                print("ЦВЗ должно быть квадратным: 32x32 или 64x64.")
                continue
            bits = (wm_img > 128).astype(np.uint8)

            ch_idx = input("Канал (0=R, 1=G, 2=B): ").strip()
            if ch_idx not in ('0', '1', '2'):
                print("Некорректный канал.")
                continue

            try:
                r = int(input("Итерации Арнольда: ").strip())
            except:
                print("Неверное число.")
                continue
            try:
                p = float(input("Порог p (0): ").strip() or 1.0)
                q = float(input("Порог q (1): ").strip() or 1.0)
                l = float(input("Параметр λ: ").strip() or 1.0)
            except:
                print("Ошибка параметров.")
                continue

            try:
                result_img, cap, ratio, stats = inject_wm(
                    host, bits, color_ch=int(ch_idx),
                    rounds=r, p_val=p, q_val=q, weight=l
                )
            except Exception as err:
                print(f"Ошибка встраивания: {err}")
                continue

            dest = input("Сохранить в: ").strip()
            try:
                write_pic(result_img, dest)
            except Exception as err:
                print(f"Ошибка сохранения: {err}")
                continue
            print(f"ЦВЗ встроен. Вместимость: {cap} бит, заполнено: {ratio*100:.2f}%")
            print(f"PSNR: {stats['psnr']:.2f} дБ, MSE: {stats['mse']:.2f}, SSIM: {stats['ssim']:.4f}")
        elif cmd == '2':
            img_path = input("Изображение с ЦВЗ: ").strip()
            try:
                encoded = load_pic(img_path)
            except Exception as err:
                print(f"Ошибка: {err}")
                continue

            ch_idx = input("Канал (0=R, 1=G, 2=B): ").strip()
            if ch_idx not in ('0', '1', '2'):
                print("Неверный канал.")
                continue
            try:
                rounds = int(input("Итерации Арнольда: ").strip())
                size = int(input("Размер ЦВЗ (N): ").strip())
            except:
                print("Неверный ввод.")
                continue
            if size not in (32, 64):
                print("Размер должен быть 32 или 64.")
                continue

            try:
                extracted = retrieve_wm(encoded, size, color_ch=int(ch_idx), rounds=rounds)
            except Exception as err:
                print(f"Ошибка извлечения: {err}")
                continue
            path = input("Куда сохранить ЦВЗ: ").strip()
            try:
                write_pic((extracted * 255).astype(np.uint8), path)
            except Exception as err:
                print(f"Ошибка: {err}")
                continue
            print("ЦВЗ извлечён и сохранён.")
        elif cmd == '3':
            print("Выход.")
            break
        else:
            print("Введите 1, 2 или 3.")

if __name__ == '__main__':
    cli()
