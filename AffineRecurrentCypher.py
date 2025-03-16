def gcd(a, b):
    if a == 0 or b == 0:
        return 0
    while b:
        a, b = b, a % b
    return a

def inv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under modulo {m}")

def check_keys(alpha1, alpha2):
    if alpha1 == 0 or alpha2 == 0:
        return False
    return True

def encrypt_affine_recursive(plaintext, alpha1, beta1, alpha2, beta2, m=26):
    l = len(plaintext)
    if gcd(alpha1, m) != 1 or gcd(alpha2, m) != 1:
        raise ValueError("Keys must have GCD of 1 with m")
    alphas = [alpha1, alpha2]
    betas = [beta1, beta2]
    cyphertext = []
    for i in range(l):
        if i >= 2:
            new_alpha = (alphas[i - 1] * alphas[i - 2]) % m
            new_beta = (betas[i - 1] + betas[i - 2]) % m
            alphas.append(new_alpha)
            betas.append(new_beta)
        if plaintext[i] == -65:
            cyphertext.append(-1)
        else:
            y_i = (alphas[i] * plaintext[i] + betas[i]) % m
            cyphertext.append(y_i)
    return cyphertext

def decrypt_affine_recursive(cyphertext, alpha1, beta1, alpha2, beta2, m=26):
    if isinstance(cyphertext, str):
        cyphertext = [ord(char) - ord('A') for char in cyphertext.upper() if char.isalpha()]
    
    l = len(cyphertext)
    if gcd(alpha1, m) != 1 or gcd(alpha2, m) != 1:
        raise ValueError("Keys must have GCD of 1 with m")
    
    alphas = [alpha1, alpha2]
    betas = [beta1, beta2]
    plaintext = []
    
    for i in range(l):
        if i >= 2:
            new_alpha = (alphas[i - 1] * alphas[i - 2]) % m
            new_beta = (betas[i - 1] + betas[i - 2]) % m
            alphas.append(new_alpha)
            betas.append(new_beta)
        
        if cyphertext[i] == -1:
            plaintext.append(-65)
        else:
            alpha_inv = inv(alphas[i], m)
            if alpha_inv is None:
                raise ValueError(f"No modular inverse for alpha={alphas[i]} mod {m}")
            x_i = (cyphertext[i] - betas[i]) * alpha_inv % m
            plaintext.append(x_i)
    
    # Преобразуем числа обратно в символы
    plaintext_str = ''.join([chr(p + ord('a')) for p in plaintext])
    return plaintext_str


def affine_recurrent_crack(ciphertext):
    alpha_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in alpha_list:
            for b in range(26):
                for c in alpha_list:
                    for d in range(26):
                        decrypted_text = decrypt_affine_recursive(ciphertext, a, b,  c, d)
                        print(decrypted_text, a, b, c, d)

if __name__ == "__main__":
    alpha1, beta1 = 1, 0
    alpha2, beta2 = 1, 0
    plaintext = []
    cypher_text = []
    while(True):
        user_input = input("> Choose what to do: e(ncrypt), d(ecrypt), k(ey), c(rack), q(uit): ").lower()
        match user_input:
            case 'q':
                print("> Shutting down...")
                break
            case 'c':
                text_to_crack = input("> Type in text to crack: ")
                print("> Possible texts:")
                cracked_text = affine_recurrent_crack(text_to_crack)
            case 'e':
                if not check_keys(alpha1, alpha2):
                    print('> You should define keys first and alphas can\'t be zeroes')
                else:
                    plaintext_input = input("> Type in plaintext to encrypt: ")
                    plaintext = [ord(c) - ord('a') for c in plaintext_input]
                    encrypted_affine_recursive_text = encrypt_affine_recursive(plaintext, alpha1, beta1, alpha2, beta2)
                    encrypt_affine_recursive_string = ''.join(chr(x + ord('a')) for x in encrypted_affine_recursive_text)
                    print(f"> Cyphered text: {encrypt_affine_recursive_string}")
            case 'd':
                if not check_keys(alpha1, alpha2):
                    print('> You should define keys first and alphas can\'t be zeroes')
                else:
                    cypher_text = input("> Type in the list of values to decrypt it to plaintext: ")
                    decrypted_text = decrypt_affine_recursive(cypher_text, alpha1, beta1, alpha2, beta2)
                    print(f"> Decrypted text: {decrypted_text}")
            case 'k':
                keys_input = input("> Type in four numbers: alpha 1, beta 1, alpha 2, beta 2: ").split(" ")
                alpha1, beta1 = int(keys_input[0]), int(keys_input[1])
                alpha2, beta2 = int(keys_input[2]), int(keys_input[3])
                print('> Keys saved')
            case _:
                print("> Input not recognised")