# Combine the two programs from exercise 10-11 into one file. If the number
# is already stored, report the favorite number to the user. If not, prompt
# for the user's favorite number and store it in a file.
import json

def get_stored_number():
    """Get user's stored favorite number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    """Prompt user for their favorite number and stores it."""
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
            return number

def read_number():
    """Reads the user's favorite number from file."""
    number = get_stored_number()
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        number = get_new_number()
        print(f"We'll remember your favorite number {number} next time.")

read_number()