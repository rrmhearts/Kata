
from itertools import cycle
from rotate_string import rotate_string_left, split_and_swap_bytearray

def des_like(message, key):
    
    # Zip with cycling the shorter string
    for n in range(len(message)):
        # Rotate key so it is unique
        k = rotate_string_left(key, n)
        zipped = zip(message, cycle(k)) if len(message) > len(k) else zip(cycle(message), k)
        message = bytes(a ^ b for a, b in zipped)
        # Swap ordering
        message = split_and_swap_bytearray(message)
    return message

def encrypt(message, key):
    # Needs to be even length
    if len(message) % 2 != 0:
        message+=b'_'
    return des_like(message, key)

def decrypt(message, key):
    plaintext = des_like(message,key)
    return plaintext[:-1] if plaintext[-1] == 95 else plaintext
        
def xor_bytes(byte_str1, byte_str2):
     # Requires both strings to be the same length
     return bytes(a ^ b for a, b in zip(byte_str1, byte_str2))

message = b'hello world, see how this goes.'
key = b'SECRET'
# Encoded message:  b'\x1b\x00\x0f\x1e\x1bS\x12\x0c\x00\x18\x17IC\x01\x11\x16E\x0b\x1d\x03S\x11\x0b\x1b\x07S\x02\x0c\x17\x07]'
encoding = encrypt(message, key)
decoded = decrypt(encoding, key)
print("Original message:", message)
print("Secret key: ", key)
print("Encoded message: ", encoding)
print("Decoded message: ", decoded)