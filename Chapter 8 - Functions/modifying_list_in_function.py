# Modifying a list in a function
# Any changes made to the list in a function are permanent, allows us to work
# efficiently with large amounts of data.

# Scenario, a company that creates 3D printed models of designs that users
# submit. Designs that need to be printed are stored in a list, and after
# being printed they're moved to a separate list. The following code does this
# without using a function.

# Start with designs that needs to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# #   Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)



## We can write two functions to cover the code.
# Each of which does one specific job.
# Function 1: handles printing the designs.
# Function 2: summarizes the prints that have been made.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following have been printed:")
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Changing functions once is more efficient than having to change code that
# are unorganized. Helps with reusability as well.

# Every function should have one specific job.

