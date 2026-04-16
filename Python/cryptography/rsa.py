def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1, temp2 = temp_phi // e, temp_phi - (temp_phi // e) * e
        temp_phi, e = e, temp2
        x, y = x2 - temp1 * x1, d - temp1 * y1
        x2, x1, d, y1 = x1, x, y1, y
    if temp_phi == 1:
        return d + phi

def encrypt(public_key, plaintext):
    key, n = public_key
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    key, n = private_key
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

p = 53
q = 59
n = p * q
phi = (p - 1) * (q - 1)
e = 3
d = mod_inverse(e, phi)

public_key = (e, n)
private_key = (d, n)

message = "HELLO"
encrypted_msg = encrypt(public_key, message)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(private_key, encrypted_msg)
print("Decrypted message:", decrypted_msg)