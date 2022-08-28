# A list of items that cannot change, Tuples.
# Python refers to values that cannot change as immutable, an immutable list is called a tuple.
# An example is if we have a rectangle that should always be a certain size, we can ensure that
# it doesn't change by using a tuple. TUPLE uses (brackets) NOT square [brackets]

dimensions = (200, 50)
print(dimensions[0], dimensions[1])

# if we try to change the item in the tuple...
## dimensions[0] = 250
# an error will occur saying "TypeError: 'tuple' object does not support item assignment"

# Tuples are defined by the presence of a comma (,) it makes it neater.
# If we want to only have one item as a tuple we'd use...
my_t = (3,)
print(my_t)

# Looping through all values of a tuple, simply use a for loop
dimensions_tuple = (250, 50)
for dimension in dimensions_tuple:
    print(dimension)

# Writing over a tuple * We cannot change an element in a tuple but we can assign a new variable
# that represents a tuple by redefining and entire tuple.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) # reassigning dimension tuple to new variable is valid
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# OVERALL tuples are a simple data structure, even simpler than a list