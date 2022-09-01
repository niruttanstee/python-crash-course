# A function doesn't have to just display its output, it can return a value
# back into the variable that is calling the it.

# Returning a SIMPLE VALUE.
# A scenario where a function takes a first and last name, and returns a neatly
# formatted full name:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Using variable to receive element from function return, i.e. full name.
musician = get_formatted_name("jimmy", "hendrix")
print(musician)