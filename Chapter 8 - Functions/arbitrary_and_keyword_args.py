# Using arbitrary keyword arguments.
# Sometimes we'll want to accept an arbitrary number of arguments but don't
# know ahead of time what kind of information it will be passed to the
# function. We can write a function that accepts as many key-value pairs as
# the calling statement provides.

# Example, building a user profile, we know we'll get information about a user
# but we're not sure what kind of information we'll receive.

# Arbitrary number of keyword arguments starts with double asterisks **args.
# The double asterisk is to create a dictionary. 
# Single asterisk is to create a tuple.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile(
    'albert', 
    'einstein',
    location='princeton',
    field = 'physics',
)

print(user_profile)

# It gets complicated but remember to always use the simplest approach that
# gets the job done.

# Often we'll see the parameter name **kwargs used to collect non specific
# keyword arguments.