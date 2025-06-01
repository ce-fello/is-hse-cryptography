import argparse
from collections import Counter
import string
from math import gcd
from functools import reduce

class VigenereCipher:
    def __init__(self, alphabet=None):
        self.alphabet = alphabet or string.ascii_uppercase
        self.alphabet_size = len(self.alphabet)
        self.char_to_index = {char: idx for idx, char in enumerate(self.alphabet)}
    
    def _prepare_key(self, key):
        return ''.join(filter(lambda x: x in self.char_to_index, key.upper()))
    
    def _prepare_text_for_analysis(self, text):
        return ''.join(filter(lambda x: x.upper() in self.char_to_index, text.upper()))
    
    def _repeat_key(self, text, key):
        key = self._prepare_key(key)
        if not key:
            raise ValueError("Ключ должен содержать хотя бы один символ алфавита")
        
        repeated_key = []
        key_len = len(key)
        alpha_count = 0
        
        for char in text:
            if char.upper() in self.char_to_index:
                repeated_key.append(key[alpha_count % key_len])
                alpha_count += 1
            else:
                repeated_key.append(char)
        
        return ''.join(repeated_key)
    
    def encrypt_decrypt(self, text, key_func, key, decrypt=False):
        gamma = key_func(text, key, decrypt)
        result = []
        
        for t, g in zip(text, gamma):
            upper_t = t.upper()
            if upper_t in self.char_to_index and g.upper() in self.char_to_index:
                t_idx = self.char_to_index[upper_t]
                g_idx = self.char_to_index[g.upper()]
                if decrypt:
                    new_idx = (t_idx - g_idx) % self.alphabet_size
                else:
                    new_idx = (t_idx + g_idx) % self.alphabet_size
                result.append(self.alphabet[new_idx] if t.isupper() else self.alphabet[new_idx].lower())
            else:
                result.append(t)
        
        return ''.join(result)
    
    def repeat_key_gamma(self, text, key, decrypt=False):
        return self._repeat_key(text, key)
    
    def self_key_plaintext_gamma(self, text, key, decrypt=False):
        prepared_key = self._prepare_key(key)
        if not prepared_key:
            raise ValueError("Ключ должен содержать хотя бы один символ алфавита")
        
        gamma = []
        alpha_chars = []
        
        for char in text:
            if char.upper() in self.char_to_index:
                alpha_chars.append(char.upper())
        
        if decrypt:
            gamma_chars = [prepared_key[0]] + alpha_chars[:-1]
        else:
            gamma_chars = [prepared_key[0]] + alpha_chars[:-1]
        
        gamma_ptr = 0
        for char in text:
            if char.upper() in self.char_to_index:
                gamma.append(gamma_chars[gamma_ptr])
                gamma_ptr += 1
            else:
                gamma.append(char)
        
        return ''.join(gamma)
    
    def self_key_ciphertext_gamma(self, text, key, decrypt=False):
        prepared_key = self._prepare_key(key)
        if not prepared_key:
            raise ValueError("Ключ должен содержать хотя бы один символ алфавита")
        
        if decrypt:
            gamma = []
            ciphertext_alpha = []
            
            for char in text:
                if char.upper() in self.char_to_index:
                    ciphertext_alpha.append(char.upper())
            
            gamma_chars = [prepared_key[0]] + ciphertext_alpha[:-1]
            gamma_ptr = 0
            for char in text:
                if char.upper() in self.char_to_index:
                    gamma.append(gamma_chars[gamma_ptr])
                    gamma_ptr += 1
                else:
                    gamma.append(char)
            
            return self.encrypt_decrypt(text, lambda t, k, d: ''.join(gamma), key, decrypt), ''.join(gamma)
        else:
            gamma = []
            result = []
            ciphertext_alpha = []
            
            gamma_chars = [prepared_key[0]]
            
            for char in text:
                upper_char = char.upper()
                if upper_char in self.char_to_index:
                    t_idx = self.char_to_index[upper_char]
                    g_idx = self.char_to_index[gamma_chars[-1]]
                    new_idx = (t_idx + g_idx) % self.alphabet_size
                    new_char = self.alphabet[new_idx]
                    result.append(new_char if char.isupper() else new_char.lower())
                    ciphertext_alpha.append(new_char)
                    gamma_chars.append(new_char)
                    gamma.append(gamma_chars[-2] if len(gamma_chars) > 1 else prepared_key[0])
                else:
                    result.append(char)
                    gamma.append(char)
            
            return ''.join(result), ''.join(gamma)

    def frequency_analysis(self, ciphertext, key_length=None):
        clean_text = self._prepare_text_for_analysis(ciphertext)
        if len(clean_text) < 50:
            return None, "Текст слишком короткий для достоверного анализа (нужно >50 символов)"
        
        def find_repeated_sequences(text, min_len=3, max_len=5):
            sequences = {}
            for seq_len in range(min_len, max_len+1):
                for i in range(len(text) - seq_len + 1):
                    seq = text[i:i+seq_len]
                    if seq in sequences:
                        sequences[seq].append(i)
                    else:
                        sequences[seq] = [i]
            return {seq: pos for seq, pos in sequences.items() if len(pos) > 1}
        
        repeated_seqs = find_repeated_sequences(clean_text)
        
        distances = []
        for positions in repeated_seqs.values():
            for i in range(1, len(positions)):
                distances.append(positions[i] - positions[i-1])
        
        def calculate_gcd(distances):
            if not distances:
                return 0
            current_gcd = distances[0]
            for d in distances[1:]:
                current_gcd = gcd(current_gcd, d)
                if current_gcd == 1:
                    break
            return current_gcd
        
        key_len_candidate = calculate_gcd(distances) if distances else 0
        
        if key_length is not None and key_length > 0:
            key_len_candidate = key_length
        elif key_len_candidate == 0:
            key_len_candidate = self._estimate_key_length(clean_text)
        
        if key_len_candidate == 0:
            return None, "Не удалось определить длину ключа"
        
        def frequency_attack(group, lang_freq):
            best_shift = 0
            best_score = -1
            for shift in range(self.alphabet_size):
                score = 0.0
                for char, count in group.items():
                    original_char = self.alphabet[(self.char_to_index[char] - shift) % self.alphabet_size]
                    score += count * lang_freq.get(original_char, 0)
                if score > best_score:
                    best_score = score
                    best_shift = shift
            return best_shift
        
        english_freq = {
            'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253,
            'E': 0.12702, 'F': 0.02228, 'G': 0.02015, 'H': 0.06094,
            'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025,
            'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929,
            'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
            'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150,
            'Y': 0.01974, 'Z': 0.00074
        }
        
        groups = [Counter() for _ in range(key_len_candidate)]
        for i, char in enumerate(clean_text):
            groups[i % key_len_candidate][char] += 1
        
        key_chars = []
        for group in groups:
            total = sum(group.values())
            if total == 0:
                key_chars.append('A')
                continue
            
            normalized_group = {char: count/total for char, count in group.items()}
            shift = frequency_attack(normalized_group, english_freq)
            key_chars.append(self.alphabet[shift])
        
        return ''.join(key_chars), f"Предполагаемая длина ключа: {key_len_candidate}"
    
    def _estimate_key_length(self, text):
        def index_of_coincidence(text):
            freq = Counter(text)
            total = len(text)
            if total <= 1:
                return 0.0
            return sum(count*(count-1) for count in freq.values()) / (total*(total-1))
        
        expected_ic = 0.0667
        min_ic_diff = float('inf')
        best_len = 0
        
        for possible_len in range(1, min(20, len(text)//10)):
            ics = []
            for i in range(possible_len):
                subgroup = text[i::possible_len]
                if len(subgroup) > 1:
                    ics.append(index_of_coincidence(subgroup))
            
            if not ics:
                continue
            
            avg_ic = sum(ics) / len(ics)
            ic_diff = abs(avg_ic - expected_ic)
            
            if ic_diff < min_ic_diff:
                min_ic_diff = ic_diff
                best_len = possible_len
        
        return best_len if best_len > 0 else 0

def main():
    parser = argparse.ArgumentParser(description="Шифр Виженера с криптоанализом")
    parser.add_argument('--mode', choices=['encrypt', 'decrypt', 'cryptanalysis'], required=True, help="Режим работы")
    parser.add_argument('--method', choices=['repeat', 'self_plain', 'self_cipher'], help="Метод выработки гаммы (не нужно для cryptanalysis)")
    parser.add_argument('--text', required=True, help="Текст для обработки")
    parser.add_argument('--key', help="Ключ шифрования (не нужен для cryptanalysis)")
    parser.add_argument('--key_length', type=int, help="Предполагаемая длина ключа (только для cryptanalysis)")
    
    args = parser.parse_args()
    
    cipher = VigenereCipher()
    
    if args.mode == 'cryptanalysis':
        key, info = cipher.frequency_analysis(args.text, args.key_length)
        print(f"Результаты криптоанализа:")
        print(info)
        if key:
            print(f"Найденный ключ: {key}")
            
            decrypted = cipher.encrypt_decrypt(
                args.text,
                cipher.repeat_key_gamma,
                key,
                decrypt=True
            )
            print(f"\nРасшифрованный текст: {decrypted}")
            english_letters = sum(c.isalpha() for c in decrypted.upper())
            if english_letters > 0:
                valid_letters = sum(1 for c in decrypted.upper() if c in cipher.char_to_index)
                percent_valid = valid_letters / english_letters * 100
                print(f"\nКачество расшифровки: {percent_valid:.1f}% английских букв")
        return
    
    if not args.method or not args.key:
        print("Для шифрования/расшифрования необходимо указать метод и ключ")
        return
    
    if args.method == 'repeat':
        result = cipher.encrypt_decrypt(
            args.text,
            cipher.repeat_key_gamma,
            args.key,
            decrypt=(args.mode == 'decrypt')
        )
    elif args.method == 'self_plain':
        result = cipher.encrypt_decrypt(
            args.text,
            cipher.self_key_plaintext_gamma,
            args.key,
            decrypt=(args.mode == 'decrypt')
        )
    elif args.method == 'self_cipher':
        if args.mode == 'encrypt':
            result, gamma = cipher.self_key_ciphertext_gamma(args.text, args.key)
        else:
            result, gamma = cipher.self_key_ciphertext_gamma(args.text, args.key, decrypt=True)
        print(f"Использованная гамма: {gamma}")
    
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()