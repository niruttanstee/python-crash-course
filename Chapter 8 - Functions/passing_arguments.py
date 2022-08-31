# Passing arguments.
# A function definition can have multiple parameters, a function call may need
# multiple arguments. You can pass arguments to your functions in a number of
# ways.

# Positional arguments.
# Argument passed the same order as they are written in the function
# definition parameters.
# Arguments must match the parameters.

def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


# You can call the function as many times as you want.
# Orders really matter in positional arguments.


# Keyword arguments.
# A name-value pair that you pass to a function. Directly associate the name
# and the value within the argument, to so there is no confusion.
