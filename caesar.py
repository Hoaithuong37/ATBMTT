def caesar_cipher(plain_text, key):
    result = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

plain_text = "PHAMHOAITHUONG"
key = 16
cipher_text = caesar_cipher(plain_text, key)
print("Cipher Text:", cipher_text)
