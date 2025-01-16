def encrypt_text(text, n, m):
    encrypted_text = []
    for char in text:
        if char.islower():  # For lowercase letters
            if char <= 'm':  # First half of the alphabet (a-m)
                shift = n * m
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:  # Second half of the alphabet (n-z)
                shift = -(n + m)
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif char.isupper():  # For uppercase letters
            if char <= 'M':  # First half of the alphabet (A-M)
                shift = -n
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:  # Second half of the alphabet (N-Z)
                shift = m ** 2
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:  # For special characters and numbers, leave unchanged
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    
    return ''.join(encrypted_text)


def decrypt_text(text, n, m):
    decrypted_text = []
    for char in text:
        if char.islower():  # For lowercase letters
            if char <= 'm':  # First half of the alphabet (a-m)
                shift = n * m
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:  # Second half of the alphabet (n-z)
                shift = -(n + m)
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        elif char.isupper():  # For uppercase letters
            if char <= 'M':  # First half of the alphabet (A-M)
                shift = -n
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:  # Second half of the alphabet (N-Z)
                shift = m ** 2
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:  # For special characters and numbers, leave unchanged
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    
    return ''.join(decrypted_text)


def verify_decryption(original_text, decrypted_text):
    return original_text == decrypted_text


# Main process
def main():
    # Reading the raw text from the file
    with open("raw_text.txt", "r") as file:
        raw_text = file.read()

    # Taking user inputs for encryption parameters
    n = int(input("Enter the value for n: "))
    m = int(input("Enter the value for m: "))
    
    # Encrypting the text
    encrypted_text = encrypt_text(raw_text, n, m)
    
    # Writing the encrypted text to a file
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)
    
    print("Encryption complete. Encrypted text written to 'encrypted_text.txt'.")
    
    # Decrypting the encrypted text
    decrypted_text = decrypt_text(encrypted_text, n, m)
    
    # Verifying the decryption
    if verify_decryption(raw_text, decrypted_text):
        print("Decryption successful. The original text and the decrypted text match.")
    else:
        print("Decryption failed. The original text and the decrypted text do not match.")

if __name__ == "__main__":
    main()
