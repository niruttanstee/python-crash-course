# Start with and existing list and make an entirely new list based on the first one.
# Instead of loops, we can use slice [:] which omits the first to last index.
# This tells Python to to make a slice that starts at the first item and ends in the last item.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # Copies using slice

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

# This omits a new seperate list, so we can in theory add individual different items to each list.
my_foods.append('pasta')
friend_foods.append('ice cream')

print(f"My foods: {my_foods}\nFriend's food: {friend_foods}")

# NOTE This does not work as this omits an association instead of copying the list
friend_foods = my_foods

# OVERALL A slice can make a seperate copy of a list not an associated one

