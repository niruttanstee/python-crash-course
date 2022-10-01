# The final listing for remember_me.py assumes either that the user has already
# entered their username or that the program is running for the first time.

# We should modify it in case the current user is not the person who last used
# the program.

# Before painting a welcome back message in greet_user(), ask the user if this
# is the correct username. If it's not, call get_new_username() to correct the
# username.

from tabnanny import check
from refactoring_v2 import *

def check_username():
    """Asks the user if the stored file is the correct username."""
    username = get_stored_username()
    prompt = f"Is {username} the correct username?"
    prompt = prompt + "\nEnter 'y' for yes or 'n' for no.\n"
    answer = input(prompt)
    if answer == 'y':
        greet_user()
    else:
        name = get_new_username()
        print(f"{name} we'll remember your name the next time you launch.")

check_username()