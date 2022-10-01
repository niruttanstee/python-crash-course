# Combining both programs into one file. When someone runs this program, we
# want to retrieve their username from memory if possible; therefore, we'll
# start with a try block that attempts to recover the username.

# If the file username.json doesn't exist, we'll have the except block prompt
# for a username and store it in username.json for the next time.
import json

# Load username, if it has been stored previously.
#   Otherwise, prompt for the username and store it.

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