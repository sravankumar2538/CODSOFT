import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    
    char_set = ""
    
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("You must select at least one type of character to include in the password.")
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password

def main():
    length = int(input("Enter the desired length of the password: "))

    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
