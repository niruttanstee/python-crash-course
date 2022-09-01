# We may need to make an argument optional in certain scenarios so that
# people using the function can choose to provide extra information only if
# they want to.

# Scenario, printing a full name function may or may not need a middle name
# parameter/argument.

# Standard way without making it optional.
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

print(get_formatted_name("jimmy", "lee", "hendrix"))


# Middle names aren't always needed, and this function will not work if we
# don't include 3 arguments. To make it work without a middle name, we set the
# default value of the middle_name to an empty string and move it to the end
# of the list of parameters (as it's a DEFAULT VALUE not a positional argument)
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

# This works because we have to enter two arguments the first name and last
# name but don't need to supply with middle name unless we need to. The only
# thing we need to be concerned is that the middle name position is at the
# last, we can counter the confusion by using keyword arguments.
print(get_formatted_name('jimmy', 'hendrix'))
print(get_formatted_name('jimmy', 'hendrix', 'lee'))
print(get_formatted_name(first_name='jimmy', middle_name='lee', last_name='hendrix'))