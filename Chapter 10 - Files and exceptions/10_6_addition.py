# One common problem when prompting for numerical output occurs when people
# provide text instead of numbers.

# When you try to convert input to an int, you'll get a ValueError.

# Write a program that prompts for two numbers. Add them together and print the
# result. Catch the ValueError if either input value is not a number, and print
# a friendly error message.

print("Please enter two numbers to add.")
print("Enter 'q' to quit the program.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("You did not enter two numbers to add.")
    else:
        print(f"{first_number} + {second_number} = {result}")

