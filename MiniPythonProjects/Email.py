import re
import string
from random import choice, randint, shuffle

def create_password(password_size) -> str:
    """
    Generate a random password with a specific length containing
    a mix of lowercase letters, uppercase letters, digits, and punctuation.
    """
    if password_size < 8 or password_size > 20:
        raise ValueError("Password size must be between 8 and 20 characters.")
    
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
    
    return ''.join(password_list)

def check_email(email):
    """
    Validate if the provided email address matches the standard email pattern.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def check_password_complexity(password):
    """
    Check if the password contains at least 3 of the following: lowercase letters,
    uppercase letters, digits, and punctuation, and its length is between 8 and 20 characters.
    """
    character_sets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]
    
    terms = sum(any(char in char_set for char in password) for char_set in character_sets)
    
    return terms >= 3 and 8 <= len(password) <= 20

class Gmail:
    def __init__(self):
        self.emails = {}
        self.logged_in = False
    
    def add_email(self, email, password):
        """
        Add a new email and password to the system after validation.
        """
        if not check_email(email):
            print("Invalid email format!")
            return
        if not check_password_complexity(password):
            print("Password is weak. Please ensure it contains at least 3 of the following: lowercase letters, uppercase letters, digits, and punctuation. It should be 8-20 characters long.")
            return
        if email in self.emails:
            print("This email is already used.")
            return
        
        self.emails[email] = password
        print("Email has been added successfully.")
    
    def login(self, email, password):
        """
        Log in with the provided email and password.
        """
        if self.logged_in:
            print("You need to log out first.")
            return
        if email not in self.emails:
            print("This email doesn't exist.")
            return
        if self.emails[email] == password:
            self.logged_in = True
            print("You have been logged in successfully.")
        else:
            print("Incorrect password.")
    
    def signout(self):
        """
        Log out the currently logged-in user.
        """
        if not self.logged_in:
            print("You are already logged out.")
            return
        
        self.logged_in = False
        print("You have been logged out successfully.")

def main():
    """
    Main function to run the Gmail simulation, handling user interactions.
    """
    gmail = Gmail()

    while True:
        print("\nWelcome to Gmail")
        print("Please follow the instructions below:")
        print("1. Add email")
        print("2. Sign in")
        print("3. Sign out")
        print("4. Exit")    

        option = input("Enter your option: ").strip()
        try:
            option = int(option)
            if option == 1:
                email = input("Enter the email address: ").strip()
                random_pass = input("Do you want us to generate a random password for you? (y/n): ").strip().lower()
                if random_pass == 'y':
                    password = create_password(randint(8, 20))
                    print(f"Your generated password is: {password}")
                else:
                    password = input("Enter your password: ").strip()
                gmail.add_email(email, password)
            elif option == 2:
                email = input("Enter the email address: ").strip()
                password = input("Enter your password: ").strip()
                gmail.login(email, password)
            elif option == 3:
                gmail.signout()
            elif option == 4:
                print("Thanks for using our email service.")
                break
            else:
                print("Invalid option. Please choose a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number corresponding to the options.")

if __name__ == "__main__":
    main()
