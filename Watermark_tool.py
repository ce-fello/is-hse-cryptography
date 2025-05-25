import numpy as np
import cv2
from scipy.fftpack import dct, idct
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
import os

def blockify(img, block_size=8):
    h, w = img.shape
    return (img.reshape(h // block_size, block_size, -1, block_size)
               .swapaxes(1, 2)
               .reshape(-1, block_size, block_size))

def unblockify(blocks, img_shape, block_size=8):
    h, w = img_shape
    reshaped = blocks.reshape(h // block_size, w // block_size, block_size, block_size)
    reshaped = reshaped.swapaxes(1, 2)
    return reshaped.reshape(h, w)

def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

def crop_to_fit(img, block_size=8):
    h, w = img.shape[:2]
    h_cropped = h - (h % block_size)
    w_cropped = w - (w % block_size)
    return img[:h_cropped, :w_cropped]

def embed_watermark(image, watermark, alpha=10):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = crop_to_fit(gray)
    blocks = blockify(gray)
    dct_blocks = np.array([dct2(block) for block in blocks])

    wm_flat = np.array([int(bit) for bit in watermark])
    wm_len = min(len(wm_flat), len(dct_blocks) - 1)

    for i in range(wm_len):
        coeff1 = dct_blocks[i][4, 3]
        coeff2 = dct_blocks[i+1][4, 3]
        diff = coeff1 - coeff2

        if wm_flat[i] == 1 and diff <= 0:
            dct_blocks[i][4, 3] += alpha
        elif wm_flat[i] == 0 and diff >= 0:
            dct_blocks[i+1][4, 3] += alpha

    modified_blocks = np.array([idct2(block) for block in dct_blocks])
    watermarked = unblockify(modified_blocks, gray.shape)
    watermarked = np.clip(watermarked, 0, 255).astype(np.uint8)
    watermarked_bgr = cv2.merge([watermarked]*3)

    return watermarked_bgr

def extract_watermark(watermarked_image, length, alpha=10):
    gray = cv2.cvtColor(watermarked_image, cv2.COLOR_BGR2GRAY)
    gray = crop_to_fit(gray)
    blocks = blockify(gray)
    dct_blocks = np.array([dct2(block) for block in blocks])

    wm_bits = []
    for i in range(length):
        coeff1 = dct_blocks[i][4, 3]
        coeff2 = dct_blocks[i+1][4, 3]
        wm_bits.append(1 if coeff1 - coeff2 > 0 else 0)

    return ''.join(map(str, wm_bits))

def calculate_metrics(original, watermarked):
    original_gray = crop_to_fit(cv2.cvtColor(original, cv2.COLOR_BGR2GRAY))
    watermarked_gray = crop_to_fit(cv2.cvtColor(watermarked, cv2.COLOR_BGR2GRAY))
    psnr_val = psnr(original_gray, watermarked_gray)
    ssim_val = ssim(original_gray, watermarked_gray)
    return psnr_val, ssim_val

def main():
    while True:
        print("Выберите действие:")
        print("1. Встроить ЦВЗ")
        print("2. Извлечь ЦВЗ")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            image_path = input("Введите путь к изображению-контейнеру: ")
            if not os.path.exists(image_path):
                print("Файл не найден!")
                return
            image = cv2.imread(image_path)
            wm_string = input("Введите бинарную строку ЦВЗ (например, 101010): ")
            alpha = int(input("Введите параметр alpha (рекомендуется 5-20): "))

            wm_image = embed_watermark(image, wm_string, alpha=alpha)
            output_path = "watermarked.png"
            cv2.imwrite(output_path, wm_image)
            print(f"Водяной знак встроен. Результат сохранен в: {output_path}")

            psnr_val, ssim_val = calculate_metrics(image, wm_image)
            print(f"PSNR: {psnr_val:.2f} дБ | SSIM: {ssim_val:.4f}")

        elif choice == '2':
            wm_image_path = input("Введите путь к изображению с ЦВЗ: ")
            if not os.path.exists(wm_image_path):
                print("Файл не найден!")
                return
            length = int(input("Введите длину встроенного ЦВЗ: "))
            alpha = int(input("Введите параметр alpha (тот же, что и при встраивании): "))
            wm_image = cv2.imread(wm_image_path)

            extracted = extract_watermark(wm_image, length, alpha)
            print("Извлечённый ЦВЗ:", extracted)

        elif choice == '3':
            print("Выход.")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
