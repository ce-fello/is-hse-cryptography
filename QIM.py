import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
import os

def calculate_metrics(original, stego):
    original = np.asarray(original).astype(np.float32)
    stego = np.asarray(stego).astype(np.float32)
    mse = np.mean((original - stego) ** 2)
    psnr = 10 * np.log10(255 ** 2 / mse) if mse != 0 else float('inf')
    ssim_val = ssim(original, stego, channel_axis=2, data_range=255)
    return psnr, mse, ssim_val

def calculate_bpp(total_bits, image_shape):
    h, w, _ = image_shape
    return total_bits / (h * w)

def calculate_ber(original_bits, extracted_bits):
    if len(original_bits) != len(extracted_bits):
        return None
    errors = sum(ob != eb for ob, eb in zip(original_bits, extracted_bits))
    return errors / len(original_bits)

def qim_embed(image: Image.Image, message: str, delta: int = 10):
    img = np.array(image)
    h, w, _ = img.shape

    bitstring = ''.join([format(ord(c), '08b') for c in message])
    max_bits = h * w * 3

    if len(bitstring) > max_bits:
        raise ValueError("Сообщение слишком большое для данного изображения.")

    flat_img = img.flatten()
    stego = flat_img.copy()

    for i in range(len(bitstring)):
        bit = int(bitstring[i])
        if bit == 0:
            stego[i] = int((stego[i] // (2 * delta)) * (2 * delta))
        else:
            stego[i] = int((stego[i] // (2 * delta)) * (2 * delta) + delta)

    stego_img = stego.reshape(img.shape)
    return Image.fromarray(stego_img.astype(np.uint8)), {'delta': delta, 'length': len(bitstring)}, bitstring

def qim_extract(stego_img: Image.Image, params):
    delta = params['delta']
    length = params['length']
    img = np.array(stego_img).flatten()
    bits = []

    for i in range(length):
        quant = img[i] % (2 * delta)
        bit = 1 if quant >= delta else 0
        bits.append(str(bit))

    bitstring = ''.join(bits)
    chars = [chr(int(bitstring[i:i+8], 2)) for i in range(0, len(bitstring), 8)]
    return ''.join(chars), bitstring

def compare_histograms(original, stego):
    original = np.array(original)
    stego = np.array(stego)
    colors = ('r', 'g', 'b')
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    for i, color in enumerate(colors):
        axs[0].hist(original[:, :, i].flatten(), bins=256, color=color, alpha=0.5, label=f'{color}-orig')
        axs[1].hist(stego[:, :, i].flatten(), bins=256, color=color, alpha=0.5, label=f'{color}-stego')

    axs[0].set_title('Оригинальная гистограмма')
    axs[1].set_title('Стего гистограмма')
    for ax in axs:
        ax.legend()
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\n----- QIM ------")
        print("1. Встраивание")
        print("2. Извлечение")
        print("3. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            img_path = input("Путь к изображению-контейнеру: ")
            message = input("Сообщение для встраивания: ")
            delta = int(input("Параметр дельта: "))

            image = Image.open(img_path).convert("RGB")
            stego_image, params, embedded_bits = qim_embed(image, message, delta)
            psnr, mse, ssim_val = calculate_metrics(image, stego_image)
            bpp = calculate_bpp(len(embedded_bits), np.array(image).shape)

            print(f"\nМетрики встраивания")
            print(f"PSNR: {psnr:.2f}")
            print(f"MSE: {mse:.2f}")
            print(f"SSIM: {ssim_val:.4f}")
            print(f"BPP: {bpp:.6f}")

            stego_path = os.path.splitext(img_path)[0] + "_stego.png"
            stego_image.save(stego_path)
            print(f"Стегоизображение сохранено как: {stego_path}")
            print(f"Параметры: {params}")

            compare_histograms(image, stego_image)

        elif choice == '2':
            img_path = input("Путь к стегоизображению: ")
            delta = int(input("Введите значение дельта: "))
            length = int(input("Длина битового сообщения: "))

            stego_img = Image.open(img_path).convert("RGB")
            message, extracted_bits = qim_extract(stego_img, {'delta': delta, 'length': length})
            print("\nИзвлечённое сообщение:")
            print(message)

            choice = input("Известно ли исходное сообщение для оценки BER? (y/n): ")
            if choice.lower() == 'y':
                original_message = input("Введите исходное сообщение: ")
                original_bits = ''.join([format(ord(c), '08b') for c in original_message])
                ber = calculate_ber(original_bits, extracted_bits)
                if ber is not None:
                    print(f"BER: {ber:.6f}")
                else:
                    print("Невозможно вычислить BER: разная длина битовых строк.")

        elif choice == '3':
            print("Выход.")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
