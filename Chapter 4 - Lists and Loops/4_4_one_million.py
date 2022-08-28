# Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
numbers = [value for value in range(1, 1_000_001)]
for number in numbers:
    print(number)
print("Done!")