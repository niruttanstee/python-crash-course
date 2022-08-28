# make a list of numbers from one to one million, and then use the function min(n) and max(n) to make your list actually starts at one and ends at one million. Also use the sum() function to see how fast Python can calculate the numbers.
numbers = [value for value in range(1, 1_000_001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
