import string
from random import choice, randint, shuffle

def creating_a_password(size_of_the_password) -> str:
    small = randint(1, size_of_the_password - 3)
    letter = randint(1, size_of_the_password - small - 2)
    digit = randint(1, size_of_the_password - small - letter - 1)
    punctuation = size_of_the_password - small - letter - digit
    
    small_letters = ''.join(choice(string.ascii_lowercase) for _ in range(small))
    capital_letters = ''.join(choice(string.ascii_uppercase) for _ in range(letter))
    digits = ''.join(choice(string.digits) for _ in range(digit))
    punctuations = ''.join(choice(string.punctuation) for _ in range(punctuation))
    
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
                password_size = input("Enter your password size (8 - 15): ")
                try:
                    password_size = int(password_size)
                    if not(8 <= password_size <= 15):
                        print("Invalid size! Please follow the instructions!")
                    else:
                        passwords.append(creating_a_password(password_size))
                        print(f"The created password is: {passwords[-1]}")
                except ValueError:
                    print("Invalid input!")
            case 2:
                print("Thanks for using our password generator.")
                break
            case _:
                print("Invalid choice! Please follow the instructions")
    except ValueError:
        print("Invalid input!")

print("Generated passwords: ")
for number_of_password, password in enumerate(passwords, start=1):
    print(f"Password {number_of_password} is: {password}")
