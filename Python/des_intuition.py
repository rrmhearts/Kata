
from itertools import cycle

def des_like(message, key):
     # Zip with cycling the shorter string
    zipped = zip(message, cycle(key)) if len(message) > len(key) else zip(cycle(message), key)
    return bytes(a ^ b for a, b in zipped)

def xor_bytes(byte_str1, byte_str2):
     # Requires both strings to be the same length
     return bytes(a ^ b for a, b in zip(byte_str1, byte_str2))

message = b'hello world, see how this goes.'
key = b'secrt'
encoding = des_like(message, key)
decoded = des_like(encoding, key)
print("Original message:", message)
print("Secret key: ", key)
print("Encoded message: ", encoding)
print("Decoded message: ", decoded)