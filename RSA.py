from sympy import mod_inverse

def rsa_encrypt_decrypt(text, p, q, r):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(r, phi_n)
    
    # Mã hóa từng ký tự
    encrypted_values = [pow(ord(c), r, n) for c in text]
    
    # Giải mã từng ký tự
    decrypted_values = [pow(C_i, d, n) for C_i in encrypted_values]
    decrypted_text = ''.join(chr(P_i) for P_i in decrypted_values)
    
    return encrypted_values, decrypted_text

# Thông tin đã cho
p = 17
q = 23
r = 5
plain_text = "thuong"

# Mã hóa và giải mã
encrypted_values, decrypted_text = rsa_encrypt_decrypt(plain_text, p, q, r)

# Hiển thị kết quả
print("Bản mã hóa:", encrypted_values)
print("Bản giải mã:", decrypted_text)