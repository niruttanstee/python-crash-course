# Using the range() function makes it easy to generate a series of numbers.
for value in range(1, 5):
    print(value) # Prints 1 -> 4 not to 5 because of the off-by-one behavior.

# To print the values from 1 to 5 inclusive we can do...
print("\n\n")
for value in range(1, 6):
    print(value)
    
# We can also only pass the range() function with one argument and it will count from 0 to the nth value specified.
print("\n\n")
for value in range(5):
    print(value)
    
# We can use the list() function to convert the range into a list.
numbers = list(range(1, 6))
print(numbers)

# We can pass a third argument to the range() function to provide its step range.
even_numbers  = list(range(2, 11, 2)) # Goes up in 2
print(even_numbers)