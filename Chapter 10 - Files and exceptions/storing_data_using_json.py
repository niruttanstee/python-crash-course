# We can store information users provide in a data structure such as lists or
# dictionaries. 

# The json module allows us to dump simple Python data structures into a file
# and load the data from that file the next time the program runs. We can
# also use json to share data between different Python programs. Even better,
# the JSON data format is not specific to Python, so we can use it on other
# programming languages.

# JSON JavasScript Object Notation format.

# Using json.dump() and json.load()
# 1. We'll write a program that stores a set of numbers and another program
# that reads these numbers back into memory. The first program will use
# json.dump() and the second program will be using json.load()

# json.dump() function takes two arguments: a piece of data to store and a
# file object it can use to store the data.

import json

numbers = [1, 2, 3, 4, 5, 6]

print("Storing files...")

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f) # numbers is the list, f is the file object

# 2. we will now write a program that uses json.load() to read the list back
# into memory.

import json

print("Reading files...")

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f) # requires json formatted file

print(numbers)