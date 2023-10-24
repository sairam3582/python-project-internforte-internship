import string
import random

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    if not (use_uppercase or use_lowercase or use_digits or use_special_chars):
        return "At least one character type must be selected for the password."

    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special_chars:
        character_set += string.punctuation

    if length < 10:
        return "Password length must be at least 10 characters."

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

    if isinstance(password, str):
        print("Error:", password)
    else:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
