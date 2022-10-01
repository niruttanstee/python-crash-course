# We can refactor the remember_me_v2.py by putting each task into its own
# function.

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None # Return None = no content = false
    else:
        return username


def get_new_username():
    """Prompt for new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username() # calls function
    if username: # if not none
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username() # calls function
        print(f"We'll remember you when you come back, {username}!")
        
# These compartmentalization of work is an essential part of writing clear code
# that will be easy to maintain and extend.