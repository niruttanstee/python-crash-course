# Python standard library is a set of modules included in every Python
# installation. Now that we have a basic understanding of how functions and
# classes work, we can use modules from other programmers to include in our
# code.

# One of the module: randint()
# A function that takes two integer arguments and returns a randomly selected
# between and including those numbers.

# Generate a number between 1 and 6
from random import randint
print(randint(1, 6))

# Another useful function is choice(). It takes the list or tuple and returns
# a randomly chosen element.

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

# External modules that isn't written by developers of the organization should
# not be used when building security-related applications.