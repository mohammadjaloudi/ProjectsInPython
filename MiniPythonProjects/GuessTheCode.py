from random import shuffle, choice, randint
from string import ascii_uppercase

def get_string_size() -> int:
    return randint(2, 5)

def get_string(size) -> str:
    string = ""
    while len(string) != size:
        char = choice(ascii_uppercase)
        if char not in string:
            string += char
    string_list = list(string)
    shuffle(string_list)
    return ''.join(string_list)

def main() -> None:
    attempts = 10
    size = get_string_size()
    code = get_string(size)
    string_chars = list(code)
    shuffle(string_chars)
    print(f"The code's characters are: {string_chars}")
    while True:
        if attempts == 0:
            print(f"""
                  You lost :(
                  The code was {code}
                  Good luck next time
                  """)
            break
        
        print(f"You have {attempts} attempts to guess the code of size {size}")
        guess = input("Enter your guess: ")
        if len(guess) != size:
            print(f"Please enter a code of size {size}")
            continue
        correct = 0
        for i in range(size):
            if guess[i] == code[i]:
                correct += 1
        if guess == code:
            print(f"""
                  You won :)
                  {attempts} attempts left
                  """)
            break
        attempts -= 1
        print(f"Your guess {guess} has {correct} correct characters in the right position. You have {attempts} attempts left.")

if __name__ == '__main__':
    main()
