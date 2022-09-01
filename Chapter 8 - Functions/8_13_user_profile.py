# Build a profile of yourself by calling build_profile(), using your first,
# last names and three other key-value paris that describes you. 

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

my_profile = build_profile('nirutt', 'anstee',
    birth_place = 'thailand',
    race = 'southeast asian',
    profession = 'software engineer'
)

print(my_profile)