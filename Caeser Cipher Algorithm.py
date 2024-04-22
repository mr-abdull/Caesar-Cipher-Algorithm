def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Get the ASCII value of the character
            ascii_val = ord(char)
            # Check if the character is uppercase or lowercase
            if char.isupper():
                # Encrypt uppercase letters
                encrypted_text += chr((ascii_val - 65 + shift) % 26 + 65)
            else:
                # Encrypt lowercase letters
                encrypted_text += chr((ascii_val - 97 + shift) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

def main():
    message = input("Enter a message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)

    decrypt_option = input("Would you like to decrypt the message? (yes/no): ")
    if decrypt_option.lower() == "yes":
        decrypted_message = caesar_cipher(encrypted_message, -shift)
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
