import binascii
import hashlib

dk = hashlib.pbkdf2_hmac(
    hash_name='sha256',
    password='bad_password34'.encode(),
    salt='bad_salt'.encode(),
    iterations=10000
)
encrypted_data = binascii.hexlify(dk)
print(encrypted_data)