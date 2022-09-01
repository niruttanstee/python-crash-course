# Sometimes we want to prevent a function from modifying a list.
# Say if we started with an unprinted designs and write a function to move
# them to a list of completed models but want to keep the original list of
# unprinted designs for your records.

# We can do this by passing a copy of the list to the function to keep the
# original unchanged.

# Remember [:] to create a copy of a list.

# Note that most of the time there isn't a point of making a copy unless you
# have a specific reason otherwise it isn't efficient as it requires extra
# ram and memory especially working with large lists.

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

# HERE IS THE COPY

print_models(unprinted_designs[:], completed_models) # on this line
show_completed_models(completed_models)
print(unprinted_designs) # still intact