# Saving data with json is useful when we're working on user generated data,
# because if we don't store the user information somehow, we'll lose it when
# the program stops running.

# This is an example to prompt the for their name the first time they run a
# program and then remember their name when they run the program again.

# 1. Store user's names
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

# We'll combine the greet_user.py to one program
