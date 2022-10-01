# Write a program that prompts for the user's favorite number. Use json.dump()
# to store this number in a file. Write a separate program that reads in this
# value and prints the message, "I know your favorite number! It's ____."
import json

def get_user_number():
    """Gets user's favorite number to store."""
    while True:
        number = input("What's your favorite number? ")
        try:
            number = int(number)
        except ValueError:
            print("Please enter a valid number.")
        else:
            filename = 'favorite_number.json'
            with open(filename, 'w') as f:
                json.dump(number, f)
            print(f"We'll remember your favorite number {number} next time!")
            break

def read_number():
    """Reads the user's favorite number from json file."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        print(f"File {filename} does not exist!")
    else:
        print(f"I know your favorite number! It's {number}.")

