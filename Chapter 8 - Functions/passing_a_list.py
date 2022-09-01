# Passing a list to a function.
# Scenario, a list of users that we want to print a greeting to each. The
# following example sends a list of names to a function called greet_users()
# which greets each person in the list individually.

def greet_users(names):
    """Prints a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)