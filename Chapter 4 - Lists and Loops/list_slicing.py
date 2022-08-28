# Work with specific group of items in the list using the slice() function.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # Print items of index 0, 1, 2 from the list.

# We can omit the slice without the first argument if we want to include all up until the second argument number e.g.
print(players[:4]) # Print items of index 0 to index 3

# we can omit the slice from a specific start point of the list until the end of the list.
print(players[3:])

# In theory we can slice the list to be able to start the group further down the index e.g. players[2:4] will start the item with index of 2 to 3.
print(players[2:4])

# We can also use the negative value to slice values from the end to front, for example... returning the items distanced from the end index value.
print(players[-3:]) # Prints the last 3 items.

# We can also use a third argument which is a STEP for which we can specify the slice function just like the range to skip the number of items.