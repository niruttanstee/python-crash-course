# Use the third argument of the range() function to make list of the odd numbers from 1 to 20. Use a for loop to print each number.
for number in range(1, 21):
    if number % 2 != 0:
        print(number)