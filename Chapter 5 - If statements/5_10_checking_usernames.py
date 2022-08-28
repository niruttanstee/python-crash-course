# Simulating how websites ensure that everyone has a unique name.
# Make a list of five or more usernames called current_users.
current_users = ['john', 'jacob', 'wicks', 'nadine', 'sasha']

# Make another list of five usernames called new_users and make sure one of
# of the new usernames are also in the current_users list.
new_users = ['jennifer', 'rosinha', 'mackenzie', 'sasha', 'lilly']

# Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username, otherwise print a message saying that the username is
# available.
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} is unavailable, please try another name.")
    else:
        print(f"{new_user} is available.")