import hashlib
import sys
import csv
import os
from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from dotenv import load_dotenv
load_dotenv()

SALT = b64decode(os.getenv('SALT'))

# SALT = get_random_bytes(AES.block_size)
def encrypt(plain_text, password):
    private_key = hashlib.scrypt(
        password.encode(), salt=SALT, n=2**14, r=8, p=1, dklen=32)
    cipher_config = AES.new(private_key, AES.MODE_GCM, nonce=SALT)
    cipher_text= cipher_config.encrypt(bytes(plain_text, 'utf-8'))
    return b64encode(cipher_text).decode('utf-8')

def decrypt(cipher_text, password):
    cipher_text = b64decode(cipher_text)
    private_key = hashlib.scrypt(
        password.encode(), salt=SALT, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=SALT)
    decrypted = cipher.decrypt(cipher_text)
    return decrypted

def encrypt_to_bin(plain_text, password, output_file):
    encrypted = encrypt(plain_text, password)
    with open(output_file, 'wb') as file:
        file.write(b64decode(encrypted))

def decrypt_from_bin(input_file, password):
    with open(input_file, 'rb') as file:
        cipher_text = file.read()
    cipher_text = b64encode(cipher_text)
    decrypted = decrypt(cipher_text, password)
    return bytes.decode(decrypted)

def read_csv_to_plaintext(file_path):
    plaintext = ""
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            plaintext += ', '.join(row) + '\n'
    return plaintext

def write_plaintext_to_csv(plaintext, file_path):
    rows = plaintext.split('\n')  # Split plaintext into rows
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            columns = row.split(', ')  # Split each row into columns
            writer.writerow(columns)

def main():
    arguments = sys.argv[1:]  # Exclude the script name
    operation = arguments[0]
    if operation == "encrypt":
        password, input_file, output_file = arguments[1:]
        plainText = read_csv_to_plaintext(input_file)
        encrypt_to_bin(plainText, password, output_file)
    elif operation == "decrypt":
        password, input_file, output_file = arguments[1:]
        try:
            decrypted = decrypt_from_bin(input_file, password)
            write_plaintext_to_csv(decrypted, output_file) 
        except:
            print("Wrong password")
    elif operation == "get_salt":
        salt = get_random_bytes(AES.block_size)
        salt = b64encode(salt).decode('utf-8')
        print(f"Your random salt is: {salt}")
    else:
        print('Unknown operation')

if __name__ == "__main__":
    main()