# Add an if test to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Otherwise print the generic greetings.
usernames = []

if usernames:
    for name in usernames:
        if name.lower() == "admin":
            print(f"Hello {name}, would you like to see the status report?")
        else: 
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")