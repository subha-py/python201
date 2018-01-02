from Crypto.Cipher import DES

key = 'abcdefgh'.encode()

def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

des = DES.new(key,DES.MODE_ECB)

text = 'Python rocks!'.encode()
padded_text = pad(text)
try:
    encrypted_text = des.encrypt(text)
except ValueError:
    print('The encryption text should be a multiple of 8')

encrypted_text = des.encrypt(padded_text)
print(encrypted_text)

decrypted_text = des.decrypt(encrypted_text)
print(decrypted_text.decode())