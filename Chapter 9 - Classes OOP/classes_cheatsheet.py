# The function that's part of a class is a METHOD.
# def __init__() REMEMBER THE DEF
# Runs whenever we create a class, so it's needed.

# The SELF parameter is required in the method definition, and it must come 
# first before the other parameters. Self is passed automatically so we don't
# need to pass any arguments when we create the class.
# Any variable prefixed with SELF is available to every method in the class,
# and we'll also be able to access these variables through any instances
# created from the class. 

# The line self.name = name takes the value associated with the parameter name
# and assigns it to the variable name, which is then attached to the instance
# being created. Variables that are accessible through instances like this
# are called attributes.

# To use the attributes from SELF, we'll need to pass SELF as a parameter
# value in any function. i.e. def function(self):

# SELF parameter is required for every function inside a class. To
# differentiate itself from other non instantiated functions