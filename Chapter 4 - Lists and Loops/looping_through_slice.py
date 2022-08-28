# we can use a slice in a for loop if we want to loop through a subset of the elements in a list.
# For this instance we loop through the first three players and print their names.
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# remember that .title() capitalises every first letter of each word