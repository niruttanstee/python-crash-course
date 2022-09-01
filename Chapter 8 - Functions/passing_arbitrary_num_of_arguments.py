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
    