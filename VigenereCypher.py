def generate_repeated_key(key: str, text_length: int) -> str:
    key = key.replace(" ", "").lower()
    if not key:
        raise ValueError("Ключ не может быть пустым")
    repeated_key = (key * (text_length // len(key) + 1))[:text_length]
    return repeated_key

def generate_self_key_plaintext(initial_key: str, plaintext: str) -> str:
    initial_key = initial_key.replace(" ", "").lower()
    plaintext = plaintext.lower()
    if not plaintext:
        return initial_key
    self_key = initial_key + plaintext[:-1]
    return self_key

def generate_self_key_ciphertext(initial_key: str, ciphertext: str) -> str:
    initial_key = initial_key.replace(" ", "").lower()
    ciphertext = ciphertext.lower()
    if not ciphertext:
        return initial_key
    self_key = initial_key + ciphertext[:-1]
    return self_key

def process_text(text: str, key_stream: str, encrypt: bool = True) -> str:
    result = []
    key_index = 0
    key_len = len(key_stream)
    
    for char in text.lower():
        if char == ' ':
            result.append(' ')
            continue
            
        if not char.isalpha():
            continue
            
        key_char = key_stream[key_index % key_len]
        key_index += 1
        
        if encrypt:
            new_char = chr((ord(char) - ord('a') + ord(key_char) - ord('a')) % 26 + ord('a'))
        else:
            new_char = chr((ord(char) - ord('a') - (ord(key_char) - ord('a'))) % 26 + ord('a'))
        
        result.append(new_char)
    
    return ''.join(result)

def vigenere_encrypt(plaintext: str, key: str, mode: str) -> str:
    plaintext = plaintext.lower()
    key = key.lower()
    
    if mode == "repeat":
        text_letters = [c for c in plaintext if c.isalpha()]
        key_stream = generate_repeated_key(key, len(text_letters))
        return process_text(plaintext, key_stream, encrypt=True)
        
    elif mode == "self_plain":
        plaintext_letters = [c for c in plaintext if c.isalpha()]
        key_stream = generate_self_key_plaintext(key, ''.join(plaintext_letters))
        return process_text(plaintext, key_stream, encrypt=True)
        
    elif mode == "self_cipher":
        plaintext_letters = [c for c in plaintext if c.isalpha()]
        ciphertext = []
        key_part = key
        
        for i, char in enumerate(plaintext_letters):
            if i < len(key_part):
                k = ord(key_part[i]) - ord('a')
            else:
                k = ord(ciphertext[i-len(key_part)]) - ord('a')
                
            encrypted_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            ciphertext.append(encrypted_char)
        
        result = []
        char_index = 0
        for c in plaintext:
            if c == ' ':
                result.append(' ')
            elif c.isalpha():
                result.append(ciphertext[char_index])
                char_index += 1
            else:
                continue
                
        return ''.join(result)

def vigenere_decrypt(ciphertext: str, key: str, mode: str) -> str:
    ciphertext = ciphertext.lower()
    key = key.lower()
    
    if mode == "repeat":
        text_letters = [c for c in ciphertext if c.isalpha()]
        key_stream = generate_repeated_key(key, len(text_letters))
        return process_text(ciphertext, key_stream, encrypt=False)
        
    elif mode == "self_plain":
        ciphertext_letters = [c for c in ciphertext if c.isalpha()]
        plaintext = []
        key_part = key
        
        for i, char in enumerate(ciphertext_letters):
            if i < len(key_part):
                k = ord(key_part[i]) - ord('a')
            else:
                k = ord(plaintext[i-len(key_part)]) - ord('a')
                
            decrypted_char = chr((ord(char) - ord('a') - k) % 26 + ord('a'))
            plaintext.append(decrypted_char)
        
        result = []
        char_index = 0
        for c in ciphertext:
            if c == ' ':
                result.append(' ')
            elif c.isalpha():
                result.append(plaintext[char_index])
                char_index += 1
            else:
                continue
                
        return ''.join(result)
        
    elif mode == "self_cipher":
        ciphertext_letters = [c for c in ciphertext if c.isalpha()]
        key_stream = generate_self_key_ciphertext(key, ''.join(ciphertext_letters))
        return process_text(ciphertext, key_stream, encrypt=False)

def get_mode_choice() -> str:
    """Выбор метода генерации ключа"""
    print("\nВыберите метод генерации ключа:")
    print("1. Повторение ключа")
    print("2. Самоключ по открытому тексту")
    print("3. Самоключ по шифртексту")
    while True:
        choice = input("Ваш выбор (1-3): ")
        if choice in {"1", "2", "3"}:
            return {
                "1": "repeat",
                "2": "self_plain",
                "3": "self_cipher"
            }[choice]
        print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3")
import re
from collections import Counter
from math import gcd
from functools import reduce
import string

# Вспомогательные функции
def preprocess_text(text: str) -> str:
    return re.sub(r'[^a-z]', '', text.lower())

def calculate_ic(text: str) -> float:
    if len(text) < 2:
        return 0.0
    counts = Counter(text)
    total = sum(n*(n-1) for n in counts.values())
    return total / (len(text) * (len(text)-1))

def find_key_length_kasiski(ciphertext: str, max_len=20) -> int:
    ciphertext = preprocess_text(ciphertext)
    sequences = {}
    
    for seq_len in range(3, 6):
        for i in range(len(ciphertext) - seq_len):
            seq = ciphertext[i:i+seq_len]
            if seq in sequences:
                sequences[seq].append(i)
            else:
                sequences[seq] = [i]
    
    distances = []
    for seq, positions in sequences.items():
        if len(positions) > 1:
            for i in range(1, len(positions)):
                distances.append(positions[i] - positions[0])
    
    if not distances:
        return 1
    
    def gcd_of_list(lst):
        return reduce(gcd, lst)
    
    likely_length = gcd_of_list(distances)
    
    if likely_length == 1:
        divisors = []
        for d in distances:
            for i in range(2, min(max_len, d//2)+1):
                if d % i == 0:
                    divisors.append(i)
        if divisors:
            likely_length = Counter(divisors).most_common(1)[0][0]
    
    return likely_length if likely_length > 0 else 1

def frequency_attack(ciphertext: str, key_length: int, lang_freq: dict) -> str:
    ciphertext = preprocess_text(ciphertext)
    key = []
    
    for i in range(key_length):
        group = ciphertext[i::key_length]
        if not group:
            continue
        
        best_shift = 0
        best_score = -1
        
        for shift in range(26):
            score = 0
            for c in group:
                decrypted = chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
                score += lang_freq.get(decrypted, 0)
            
            if score > best_score:
                best_score = score
                best_shift = shift
        
        key.append(chr(best_shift + ord('a')))
    
    return ''.join(key)

ENGLISH_FREQ = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974,
    'z': 0.074
}

def analyze_repeated_key(ciphertext: str) -> dict:
    result = {}
    ciphertext_clean = preprocess_text(ciphertext)
    
    key_length = find_key_length_kasiski(ciphertext_clean)
    result['key_length'] = key_length
    
    if key_length > 0:
        likely_key = frequency_attack(ciphertext_clean, key_length, ENGLISH_FREQ)
        result['likely_key'] = likely_key
        
        decrypted = vigenere_decrypt(ciphertext, likely_key, "repeat")
        result['decrypted_sample'] = decrypted[:100] + "..." if len(decrypted) > 100 else decrypted
    
    return result

def analyze_self_key_plaintext(ciphertext: str, known_plain_start: str = "") -> dict:
    result = {}
    ciphertext_clean = preprocess_text(ciphertext)
    
    if known_plain_start:
        known_plain_start = preprocess_text(known_plain_start)
        if len(known_plain_start) > 0:
            recovered_key = known_plain_start[0]
            recovered_plain = known_plain_start
            
            for i in range(len(known_plain_start)):
                if i < len(recovered_key):
                    k = ord(recovered_key[i]) - ord('a')
                else:
                    k = ord(recovered_plain[i-len(recovered_key)]) - ord('a')
                
                decrypted_char = chr((ord(ciphertext_clean[i]) - ord('a') - k) % 26 + ord('a'))
                recovered_plain += decrypted_char
            
            result['recovered_key_start'] = recovered_key
            result['recovered_plain_start'] = recovered_plain
    
    else:
        possible_keys = string.ascii_lowercase
        best_score = -1
        best_key = ''
        best_plain = ''
        
        for key_candidate in possible_keys:
            plain_candidate = ''
            current_key = key_candidate
            
            for i in range(min(20, len(ciphertext_clean))):
                k = ord(current_key[i]) - ord('a') if i < len(current_key) else ord(plain_candidate[i-len(current_key)]) - ord('a')
                decrypted_char = chr((ord(ciphertext_clean[i]) - ord('a') - k) % 26 + ord('a'))
                plain_candidate += decrypted_char
            
            score = sum(ENGLISH_FREQ.get(c, 0) for c in plain_candidate)
            if score > best_score:
                best_score = score
                best_key = key_candidate
                best_plain = plain_candidate
        
        result['likely_initial_key'] = best_key
        result['likely_plain_start'] = best_plain
    
    return result

def analyze_self_key_ciphertext(ciphertext: str, known_plain_start: str = "") -> dict:
    result = {}
    ciphertext_clean = preprocess_text(ciphertext)
    
    if known_plain_start:
        known_plain_start = preprocess_text(known_plain_start)
        if len(known_plain_start) > 0:
            recovered_key = known_plain_start[0]
            recovered_plain = known_plain_start
            
            for i in range(len(known_plain_start)):
                if i < len(recovered_key):
                    k = ord(recovered_key[i]) - ord('a')
                else:
                    k = ord(ciphertext_clean[i-len(recovered_key)]) - ord('a')
                
                decrypted_char = chr((ord(ciphertext_clean[i]) - ord('a') - k) % 26 + ord('a'))
                recovered_plain += decrypted_char
            
            result['recovered_key_start'] = recovered_key
            result['recovered_plain_start'] = recovered_plain
    
    else:
        first_chars = [ciphertext_clean[0]] if ciphertext_clean else []
        best_score = -1
        best_key = ''
        
        for key_candidate in string.ascii_lowercase:
            k = ord(key_candidate) - ord('a')
            decrypted_char = chr((ord(first_chars[0]) - ord('a') - k) % 26 + ord('a')) if first_chars else ''
            score = ENGLISH_FREQ.get(decrypted_char, 0)
            
            if score > best_score:
                best_score = score
                best_key = key_candidate
        
        result['likely_initial_key'] = best_key
        
        if ciphertext_clean:
            plain_candidate = ''
            current_key = best_key
            
            for i in range(min(20, len(ciphertext_clean))):
                if i < len(current_key):
                    k = ord(current_key[i]) - ord('a')
                else:
                    k = ord(ciphertext_clean[i-len(current_key)]) - ord('a')
                
                decrypted_char = chr((ord(ciphertext_clean[i]) - ord('a') - k) % 26 + ord('a'))
                plain_candidate += decrypted_char
            
            result['likely_plain_start'] = plain_candidate
    
    return result

def main():
    current_key = "secret"
    while True:
        print(f"Текущий ключ: {current_key}")
        print("1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("3. Изменить ключ")
        print("4. Анализ шифртекста (взлом)")
        print("5. Выход")
        
        action = input("Выберите действие (1-5): ").strip()
        
        match action:
            case "1":
                plaintext = input("Введите текст для шифрования: ")
                mode = get_mode_choice()
                try:
                    ciphertext = vigenere_encrypt(plaintext, current_key, mode)
                    print(f"Зашифрованный текст: {ciphertext}")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                
            case "2":
                ciphertext = input("Введите текст для расшифрования: ")
                mode = get_mode_choice()
                try:
                    plaintext = vigenere_decrypt(ciphertext, current_key, mode)
                    print(f"Расшифрованный текст: {plaintext}")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                
            case "3":
                while True:
                    new_key = input("Введите новый ключ (только буквы a-z): ").lower()
                    if all(c.isalpha() or c.isspace() for c in new_key) and any(c.isalpha() for c in new_key):
                        current_key = new_key
                        print("Ключ успешно изменён!")
                        break
                    print("Ошибка: ключ должен содержать только буквы a-z (пробелы игнорируются)")
                    
            case "4":
                ciphertext = input("Введите шифртекст для анализа: ")
                mode = input("Выберите метод генерации ключа (repeat/self_plain/self_cipher): ").strip().lower()
                
                if mode == "repeat":
                    result = analyze_repeated_key(ciphertext)
                    print("\nРезультаты анализа (повторяющийся ключ):")
                    print(f"Предполагаемая длина ключа: {result.get('key_length', 'не определена')}")
                    print(f"Наиболее вероятный ключ: {result.get('likely_key', 'не определён')}")
                    print(f"Пример расшифровки: {result.get('decrypted_sample', 'нет данных')}")
                
                elif mode == "self_plain":
                    known = input("Известно начало открытого текста (если есть, иначе Enter): ")
                    result = analyze_self_key_plaintext(ciphertext, known)
                    print("\nРезультаты анализа (самоключ по открытому тексту):")
                    if known:
                        print(f"Восстановленный начальный ключ: {result.get('recovered_key_start', 'не определён')}")
                        print(f"Восстановленный текст: {result.get('recovered_plain_start', 'нет данных')}")
                    else:
                        print(f"Наиболее вероятный начальный ключ: {result.get('likely_initial_key', 'не определён')}")
                        print(f"Пример расшифровки: {result.get('likely_plain_start', 'нет данных')}")
                
                elif mode == "self_cipher":
                    known = input("Известно начало открытого текста (если есть, иначе Enter): ")
                    result = analyze_self_key_ciphertext(ciphertext, known)
                    print("\nРезультаты анализа (самоключ по шифртексту):")
                    if known:
                        print(f"Восстановленный начальный ключ: {result.get('recovered_key_start', 'не определён')}")
                        print(f"Восстановленный текст: {result.get('recovered_plain_start', 'нет данных')}")
                    else:
                        print(f"Наиболее вероятный начальный ключ: {result.get('likely_initial_key', 'не определён')}")
                        print(f"Пример расшифровки: {result.get('likely_plain_start', 'нет данных')}")
                
                else:
                    print("Неверный метод генерации ключа")
                    
            case "5":
                print("Выход из программы...")
                break
                
            case _:
                print("Неверный ввод. Пожалуйста, выберите 1-5")

if __name__ == "__main__":
    main()