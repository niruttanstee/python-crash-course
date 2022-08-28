# If we don't know the index of the item in the list we can use the remove() method which searches for the right item and removes it from the list.
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# We can also use a value defined to a variable and print a statement to why the item is removed e.g.
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me so I removed it.")

# The remove() method deletes ONLY the FIRST OCCURRENCES of the value we specify. If there are more than one of the same values in the list then we will need to use a loop instead.