# Every function should have a comment that explains concisely what the
# function does. This comment should appear immediately after the function
# definition and use the docstring format. Programmers can just read the
# docstring to understand the function to trust that the code works.

# If you define a default parameter value, there should be NO SPACES on either
# side of the equal sign.

def function_name(parameter_0, parameter_1='default value'): # like this
    return

# the same convention for keyword arguments in function calls
function_name("value_0", parameter_1="value")

# If a set of parameter of a function is longer than 79 characters this is
# how it should be formatted. Press ENTER after the opening parenthesis.
# On the next line we press TAB twice to separate the list of argument from
# the function body.

def function_name(
        parameter_0, parameter_1, parameter_2, parameter_3, parameter_4,
        parameter_5, parameter_6, parameter_7):
    return

# ALL import statements should be a the beginning of the file.