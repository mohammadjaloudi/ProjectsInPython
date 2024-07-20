import string
from random import choice, randint, shuffle

def create_password(password_size) -> str:
    s_letters = randint(1, password_size - 3)
    l_letters = randint(1, password_size - s_letters - 2)
    digits_count = randint(1, password_size - s_letters - l_letters - 1)
    punctuations_count = password_size - s_letters - l_letters - digits_count
    
    small_letters = ''.join(choice(string.ascii_lowercase) for _ in range(s_letters))
    capital_letters = ''.join(choice(string.ascii_uppercase) for _ in range(l_letters))
    digits = ''.join(choice(string.digits) for _ in range(digits_count))
    punctuations = ''.join(choice(string.punctuation) for _ in range(punctuations_count))
    
    password_characters = small_letters + capital_letters + digits + punctuations
    
    password_list = list(password_characters)
    shuffle(password_list)
    password = ''.join(password_list)
    
    return password

passwords = []

while True:
    print("\nWelcome to our password generator")
    print("Please choose your option: ")
    print("1. Create password")
    print("2. Exit")
    
    option = input("Enter your choice: ")
    
    try:
        option = int(option)
        match option:
            case 1:
                password_size = input("Enter your password size (8 - 20): ")
                try:
                    password_size = int(password_size)
                    if not(8 <= password_size <= 20):
                        print("Invalid size! Please follow the instructions!")
                    else:
                        passwords.append(create_password(password_size))
                        print(f"The created password is: {passwords[-1]}")
                except ValueError:
                    print("Invalid input! Please enter a valid number for the password size.")
            case 2:
                print("Thanks for using our password generator.")
                break
            case _:
                print("Invalid choice! Please follow the instructions.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if not passwords:
    print("No passwords exist :(")
else:
    print("Generated passwords: ")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx} is: {password}")
