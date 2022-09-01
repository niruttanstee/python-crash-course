# Passing an ARBITRARY number of arguments.
# Sometimes you won't know ahead of time how many arguments a function needs
# to accept. Fortunately, Python allows a function to collect an arbitrary
# number of arguments from the calling statement.

# Consider a function that builds a pizza. It needs to accept a number of
# toppings, but you can't know ahead of time how many toppings a person will
# want. The function in the following example has one parameter, *toppings,
# this is a SPECIAL PARAMETER as it collects as many arguments as the calling
# line provides.

def make_pizza(*toppings): # add an asterisk as a parameter field
    """Prints the pizza toppings that have been requested."""
    print(toppings)

# The asterisk in the parameter name *toppings tells Python to make a tuple
# called toppings and pack whatever values it receives into this tuple. Even
# if function creates one value.

make_pizza('pepperoni')

# We can change it into so the function loops through the list of toppings
# and describes the pizza being ordered.

def make_pizza(*toppings): # add an asterisk as a parameter field
    """Prints the pizza toppings that have been requested."""
    for topping in toppings:
        print(f"- {topping}")

make_pizza('cheddar', 'chicken', 'bbq sauce')

