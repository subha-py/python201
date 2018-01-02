from cryptography.fernet import Fernet

cipher_key = Fernet.generate_key()
print(cipher_key)

cipher = Fernet(cipher_key)
text = 'My super secret message'.encode()
encrypted_text = cipher.encrypt(text)
print(encrypted_text)

decrypt_text = cipher.decrypt(encrypted_text)
print(decrypt_text)