# Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2 and 3.

# Store the numbers 1 through 9 in a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the list. Use an if-elif-else chain inside the loop to print
# the proper ordinal ending for each number.
for number in numbers:
    if number == 1:
        ordinal = "st"
    elif number == 2:
        ordinal = "nd"
    elif number == 3:
        ordinal = "rd"
    else:
        ordinal = "th"
    
    print(f"{number}{ordinal}")