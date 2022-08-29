# Modify your program so each person can have more than one favorite number.
# Then print each person's name along with their favorite numbers. 

favorite_numbers = {
    'nadine': [22, 2, 24],
    'jacob': [55, 555, 5, 500],
    'john': [99, 999, 9999],
    'halsey': [345, 567, 2],
    'marine': [992, 83, 34], 
}

for name, numbers in sorted(favorite_numbers.items()):
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

