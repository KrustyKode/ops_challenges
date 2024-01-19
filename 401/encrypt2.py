#!/usr/bin/python3


# Script Name:                  encrypt.py
# Author:                       Michael Sineiro
# Date of latest revision:      1/16/2024
# Purpose:                      encrypts and decrypts files + messages
###                             I used chatgpt to help me write this

import os
from cryptography.fernet import Fernet
import zipfile

# Generate a new encryption key
def generate_key():
    return Fernet.generate_key()

# Load an existing encryption key or create a new one
def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        key = generate_key()
        save_key(key)
        return key

# Save the encryption key to a file
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Remove quotes from file path, if present
def sanitize_file_path(file_path):
    return file_path.strip("\"'")

# Encrypt a single file
def encrypt_file(file_path, key):
    file_path = sanitize_file_path(file_path)
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Decrypt a single file
def decrypt_file(file_path, key):
    file_path = sanitize_file_path(file_path)
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Recursively encrypt all files in a folder
def encrypt_folder(folder_path, key):
    folder_path = sanitize_file_path(folder_path)
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Recursively decrypt all files in a folder
def decrypt_folder(folder_path, key):
    folder_path = sanitize_file_path(folder_path)
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

# Encrypt a text message
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

# Decrypt a text message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message.encode()).decode()

# Compress a file into a zip archive
def compress_file(file_path):
    file_path = sanitize_file_path(file_path)
    with zipfile.ZipFile(file_path + ".zip", "w") as zipf:
        zipf.write(file_path, os.path.basename(file_path))

# Main function to handle user interaction
def main():
    key = load_key()

    print("Select a mode:")
    print("1: Encrypt a file")
    print("2: Decrypt a file")
    print("3: Encrypt a message")
    print("4: Decrypt a message")
    print("5: Encrypt a folder")
    print("6: Decrypt a folder")
    mode = input("Enter mode (1-6): ")

    if mode == '1':
        file_path = input("Enter the file path to encrypt: ")
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
        if input("Do you want to compress the output file? (y/n): ") == 'y':
            compress_file(file_path)
            print("File compressed successfully.")

    elif mode == '2':
        file_path = input("Enter the file path to decrypt: ")
        decrypt_file(file_path, key)
        print("File decrypted successfully.")

    elif mode == '3':
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message, key)
        print(f"Encrypted message: {encrypted_message}")

    elif mode == '4':
        encrypted_message = input("Enter the encrypted message to decrypt: ")
        try:
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif mode == '5':
        folder_path = input("Enter the folder path to encrypt: ")
        encrypt_folder(folder_path, key)
        print("Folder encrypted successfully.")

    elif mode == '6':
        folder_path = input("Enter the folder path to decrypt: ")
        decrypt_folder(folder_path, key)
        print("Folder decrypted successfully.")

    else:
        print("Invalid mode selected. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
