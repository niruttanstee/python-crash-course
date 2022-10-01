# Refactoring is the form of improving code that is working i.e breaking it 
# up into series of functions that have specific jobs. Makes code cleaner,
# easier to understand, and easier to extend. 

# Let's refactor our previous program: remember_me_v2.py

import json

def greet_user():
    """
    Greet user by name if username data is stored.
    Otherwise, asks user for their username to be stored.
    """
    filename = 'username.json'
    try:
        # read
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        # write
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        # passed the try-except block       
        print(f"Welcome back, {username}!")

# Call function
greet_user()

# We can refactor even more by separating each task to one separate function.