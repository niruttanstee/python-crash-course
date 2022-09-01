# Storing your functions in modules.
# Storing functions in separate files called modules and then IMPORTING them
# into the main program to be used. An IMPORT statement tells Python to make
# the code in a module available in the currently running program file.

# We can share those files with other programmers without having to share your
# entire program. We can also import libraries from other programmers as well.

# Importing an ENTIRE MODULE - in pizza.py
import pizza # time imports all functions in pizza.py file and copy it into this program
# now we use it... we call the module followed by a dot and the name of the 
# function to call
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# module_name.function_name()


# Importing SPECIFIC FUNCTIONS
# this is the syntax for this approach:
# from module_name import function_name, function_name
# as many functions as we want separated by a comma.
# as an example
from pizza import make_pizza

make_pizza(16, 'plain') # We won't need fot notations because we are importing 
# the specific function.
make_pizza(12, 'mushroom', 'chicken', 'extra cheese')


# Using AS to give FUNCTION an ALIAS
# The name of the function we want to import may be conflicted with an
# existing function in the program or if the function name is too long.
# We can use a short unique alias. i.e a nickname.
# In this example we give the function make_pizza() and alias mp() by importing
# make_pizza as mp. It renames the function.
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushroom', 'green peppers', 'extra cheese')
# form module_name import function_name as fn


# Using AS to give a MODULE an ALIAS
# We can provide an alias for a module name, giving a nickname for a module
# can allow us to call modules more quickly i.e it's more concise (brief) but
# comprehensive way to do this: p.make_pizza() then pizza.make_pizza()

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# import module_name as mn

# Importing ALL functions in a module
from pizza import * # the asterisks tell python to copy every function.

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')


# The best approach is to import the functions that you want not ALL unless
# you really are using all of it.