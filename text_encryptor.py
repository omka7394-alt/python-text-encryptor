def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

while True:
    print("\n1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        text = input("Enter message: ")
        key = int(input("Enter key number: "))
        print("Encrypted:", encrypt(text, key))
    elif choice == '2':
        text = input("Enter encrypted message: ")
        key = int(input("Enter key number: "))
        print("Decrypted:", decrypt(text, key))
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
