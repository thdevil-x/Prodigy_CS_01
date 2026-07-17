import os

# -----------------------------
# Caesar Cipher Functions
# -----------------------------

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:

        if char.isalpha():

            start = ord('A') if char.isupper() else ord('a')

            new_char = chr((ord(char) - start + shift) % 26 + start)

            result += new_char

        else:
            result += char

    return result


# -----------------------------
# Brute Force
# -----------------------------

def brute_force(cipher):
    print("\nPossible Messages:\n")

    for shift in range(26):
        text = caesar_cipher(cipher, shift, "decrypt")
        print(f"Shift {shift:2}: {text}")


# -----------------------------
# Save Output
# -----------------------------

def save_output(content):

    os.makedirs("Output", exist_ok=True)

    with open("Output/result.txt", "a") as file:
        file.write(content + "\n")

    print("\nResult saved in Output/result.txt")


# -----------------------------
# Main Program
# -----------------------------

def main():

    while True:

        print("\n" + "=" * 45)
        print("      CAESAR CIPHER TOOL")
        print("=" * 45)

        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            message = input("Enter message: ")

            try:
                shift = int(input("Enter shift value (0-25): "))
            except ValueError:
                print("Shift must be an integer.")
                continue

            encrypted = caesar_cipher(message, shift)

            print("\nEncrypted Message:")
            print(encrypted)

            save_output(f"Encrypted: {encrypted}")

        elif choice == "2":

            message = input("Enter encrypted message: ")

            try:
                shift = int(input("Enter shift value (0-25): "))
            except ValueError:
                print("Shift must be an integer.")
                continue

            decrypted = caesar_cipher(message, shift, "decrypt")

            print("\nDecrypted Message:")
            print(decrypted)

            save_output(f"Decrypted: {decrypted}")

        elif choice == "3":

            message = input("Enter encrypted message: ")

            brute_force(message)

        elif choice == "4":

            print("\nThank you for using Caesar Cipher Tool.")
            break

        else:

            print("\nInvalid choice.")


if __name__ == "__main__":
    main()