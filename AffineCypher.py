def gcd(a, b):
    if a == 0 or b == 0:
        return 0
    while b:
        a, b = b, a % b
    return a

def inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    encrypted_text = ''
    m = 26
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((a * (ord(char) - offset) + b) % m + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def affine_decrypt(text, a, b):
    decrypted_text = ''
    m = 26
    a_inv = inv(a, m)
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((a_inv * ((ord(char) - offset) - b)) % m + offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def affine_crack(ciphertext):
    alpha_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in alpha_list:
            for b in range(26):
                decrypted_text = affine_decrypt(ciphertext, a, b)
                print(decrypted_text, a, b)

if __name__ == "__main__":
    a, b = 1, 0
    while True:
        user_input = input("> Choose what to do: e(ncrypt), d(ecrypt), k(ey), c(rack), q(uit): ").lower()
        match user_input:
            case 'q':
                print("> Shutting down...")
                break
            case 'k':
                try:
                    a = int(input("> Type in the value of 'a' (must have GCD equals to 1 with 26): "))
                    b = int(input("> Type in the value of 'b': "))
                    if gcd(a, 26) != 1:
                        print("> 'a' (must have GCD equals to 1 with 26")
                        continue
                    print('> Key saved')
                except ValueError as e:
                    print(f"> Input error: {e}. Please, try again")
            case 'c':
                text_to_crack = input("> Type in text to crack: ")
                print("> Possible texts:")
                affine_crack(text_to_crack)
            case 'e':
                text_to_encrypt = input("> Type in text to encrypt: ")
                encrypted_text = affine_encrypt(text_to_encrypt, a, b)
                print(f"> Encrypted text: {encrypted_text}")
            case 'd':
                text_to_decrypt = input("> Type in text to decrypt: ")
                decrypted_text = affine_decrypt(text_to_decrypt, a, b)
                print(f"> Decrypted text: {decrypted_text}")
            case _:
                print("> Input not recognised")
        
