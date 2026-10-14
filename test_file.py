from aes_crypto import generate_key
from file_crypto import encrypt_file, decrypt_file


key = generate_key()

with open("test.txt", "rb") as file:
    original_data = file.read()

print("Original file:")
print(original_data.decode("utf-8"))

encrypted_data = encrypt_file(original_data, key)

print("\nFile encrypted successfully!")

decrypted_data = decrypt_file(encrypted_data, key)

print("\nDecrypted file:")
print(decrypted_data.decode("utf-8"))

with open("decrypted_test.txt", "wb") as file:
    file.write(decrypted_data)

print("\nDecrypted file saved as: decrypted_test.txt")