def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(start + (ord(char) - start - shift_amount) % 26)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        print("Caesar Cipher Encryption/Decryption")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '3':
            print("Exiting...")
            break
        
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == '1':
            encrypted_text = encrypt_caesar_cipher(text, shift)
            print(f"Encrypted text: {encrypted_text}")
        elif choice == '2':
            decrypted_text = decrypt_caesar_cipher(text, shift)
            print(f"Decrypted text: {decrypted_text}")
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
