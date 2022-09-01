# Missing argument error will occur if we don't provide an argument to a 
# function parameter.

def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")

describe_pet()