# Generating a list in one line. It is good to become efficient in this.

# define the name of the list variable
# squares = brackets -> [(1), (2)]
# (1) define the value of expression you want to store
# (2) write the for loop e.g. with a range to feed the values through, no need for colon.

squares = [value**2 for value in range(1, 11)]
print(squares)

even_numbers = [value for value in range(2, 22, 2)]
print(even_numbers)