# Removing items at certain positions of the list.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# we can use 'del' for this. Del is a statement and can be used as long as we know the index of the item we want to delete.
del motorcycles[0] 
print(motorcycles)

# Example above now means that we can't access the item that has been deleted.
# Removing an item using the pop() method, pop allows the last item to be removed from the list but also be able to use the value that you just 'popped'.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# This enables us to use the item e.g. removing and getting the coordinates of an alien that the user just destroyed to show an explosion.

# If list are stored in chronological order we can see which latest item in the list that has been popped.
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle this person has owned was a {last_owned.title()}.")

# We can also pop(index) to remove any items from a certain position by putting the index in the pop parentheses.
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle this person has owned was a {first_owned.title()}.")

# *If you want to remove an item and not use it, use the del statement otherwise if you want to use the item as you remove it then use the pop() method.
