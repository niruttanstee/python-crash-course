# A function is a block of code that specializes in one thing, maintainable
# and reusable. We can CALL the function to run the block of code with
# arguments/parameters called PASSING INFORMATION into functions.

# The we'll learn to store functions in separate files called MODULES    to help
# organize your main program files.

# Defining a function, a simple function named greet_user()
def greet_user(): # Function title
    """Display a simple greeting.""" # Docstring enclosed in triple quotes.
    print("Hello!") # Body of the function / wrapped by the function

greet_user() # Calls the function


# Passing information into a function.
# Passing a username to greet the user.
def greet_user(username):
    """
    Display a simple greeting to the user.
    Param: username
    """
    print(f"Hello, {username.title()}!")

greet_user('heisenberg')


# Arguments and Parameters.
# The variable username in the definition of the function is a PARAMETER
# The value 'heisenberg' is an example of an ARGUMENT, a piece of information
# that's passed from a function call to a function.

# We assign the argument value to the parameter username.