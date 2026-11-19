# Your task has been made easy, 
# as the encryption key consists of three lower case characters. 
# Using 0059_cipher.txt (right click and 'Save Link/Target As...'), 
# a file containing the encrypted ASCII codes, 
# and the knowledge that the plain text must contain common English words, 
# decrypt the message and find the sum of the ASCII values in the original text.

import string

path = r"C:\Users\LOQ\Code\euler\data\0059_cipher.txt"

def cipher(file):
    with open(file, 'r', encoding="utf-8") as f:
        content = f.read()

    ls = [int(n) for n in content.split(",")]
    return ls

def key_list():
    alph = string.ascii_lowercase
    keys = []

    for a in alph:
        for b in alph:
            for c in alph:
                keys.append(a + b + c)

    return keys

def decrypt(cipher, key):
    decrypted = []

    for i in range(len(cipher)):
        key_char = key[i % len(key)]
        decrypted_char = cipher[i] ^ ord(key_char)
        decrypted.append(chr(decrypted_char))

    return ''.join(decrypted)

def is_valid_text(text):
    common_words = [" the ", " and ", " of ", " to ", " in ", " is "]

    return (
        all(char.isprintable() or char in "\n\r\t" for char in text)
        and sum(text.count(word) for word in common_words) >= 5
    )

def main():
    encrypted = cipher(path)
    keys = key_list()

    for key in keys:
        decrypted = decrypt(encrypted, key)

        if is_valid_text(decrypted):
            print("Key:", key)
            print("Decrypted text:")
            print(decrypted)

            ascii_sum = sum(ord(char) for char in decrypted)
            print("ASCII sum:", ascii_sum)
            return

    print("No valid key found.")

if __name__ == "__main__":
    main()