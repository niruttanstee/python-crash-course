# Write a program that polls users about their dream vacation. Write a prompt
# similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

# Dictionary to store polling information
dream_vacation = {}

# Active flag while polling user
is_polling = True

# While loop to poll user name and their vacation location
while is_polling:
    name = input("What is your name?: ")
    location = input("If you could visit one place in the world, where would"
    + " you go?: ")
    
    dream_vacation[name] = location

    # Repeat option
    repeat = input("Do you want to add another user? (yes/no): ")
    if repeat == "no":
        is_polling = False

# Poll results
print("--- Dream Vacation Poll Results ---")
for name, location in dream_vacation.items():
    print(f"{name.title()}: {location}")