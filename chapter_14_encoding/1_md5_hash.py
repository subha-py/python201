import hashlib
md5 = hashlib.md5()
try:
    md5.update('Python Rocks!')
except TypeError:
    print('Unicode objects should be encoded before hashing')

test_str='Python Rocks!'.encode()
md5.update(test_str)
encrypted_data = md5.digest()
print(encrypted_data)


hex_encrypted_data = md5.hexdigest()
print(hex_encrypted_data)

sha = hashlib.sha1()
sha.update(test_str)
encrypted_data = sha.digest()
print(encrypted_data)

hex_encrypted_data = sha.hexdigest()
print(hex_encrypted_data)