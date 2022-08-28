# Sometimes we want a list to be sorted. There are various ways we can do that.
# We can use the sort() method to enable us to permanently sort our list alphabetically.

cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus']
cars.sort() # after calling this method we can't revert back to the last order
print(cars)

# We can also sort this in reverse alphabetical order as well by passing the argument reverse = True in the sort() method e.g.
cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus']
cars.sort(reverse=True)
print(cars)

# To temporary sort a list in alphabetical order and still keep the original order we can use the sorted(list_name) method, this also accepts the reverse = True argument. Sorted() takes the list as an argument.
cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus']
print(f"Here's a list of sorted cars {sorted(cars)}")
print(f"Here's a list of the original unsorted cars {cars}")

# Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase.

# Printing a list in reverse order using the reverse() method. This changes the list permanently but you can revert back to the previous original order by using the reverse() method again.
cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus']
print(cars)
cars.reverse()
print(cars)

# Getting the length of a list by using the len(list) method. This helps identify the number of items in the list for example, the number of aliens left to shoot down, among other tasks. *Python count the items in lists starting with one so we don't have to concern ourselves with one-off errors.
cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus']
print(len(cars))