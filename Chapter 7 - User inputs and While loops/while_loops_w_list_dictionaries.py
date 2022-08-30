# While loops are better if you need to modify the items while looping.
# You can't modify items during the loop using a for loop.

# Moving items from one list to another.
# Scenario, moving unverified users to the verified list after verification.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop() # pop removes and returns the last item of the list by default

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())



# Removing all instances of specific values from a list
# If we have a list of pets with the value of 'cat' repeated several times.
# To remove all instances of that value, you can run a while loop until 'cat'
# is no longer in the list.

pets = ['dog', 'cat', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f"\n{pets}")

while 'cat' in pets:
    pets.remove('cat')

print(pets)
