# We can create any set of numbers we want using the range() function. For example, we can make a list of the first 10 square numbers. By using the (**) asterisks which represents the exponents.
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
print(squares)

# We can write this more concisely by omitting the temporary variable square and appending it directly to the list...
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# Write clear code first then work on making code more efficient and concise.