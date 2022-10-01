# 2. We'll write a program that greets a user whose name has already been
# stored.

import json

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")