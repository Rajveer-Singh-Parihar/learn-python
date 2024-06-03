def encode_message(message, shift):
    encoded = ''
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encoded += chr(shifted)
        else:
            encoded += char
    return encoded

def decode_message(message, shift):
    return encode_message(message, -shift)

def main():
    while True:
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the message to encode: ")
            shift = int(input("Enter the shift value: "))
            encoded_message = encode_message(plaintext, shift)
            print(f"Encoded message: {encoded_message}\n")
        elif choice == '2':
            encoded_text = input("Enter the message to decode: ")
            shift = int(input("Enter the shift value: "))
            decoded_message = decode_message(encoded_text, shift)
            print(f"Decoded message: {decoded_message}\n")
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
