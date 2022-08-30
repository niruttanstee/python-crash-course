# Filling a dictionary with user input.
# Polling the user and storing the data into a dictionary.

responses = {}

# Set flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would like to climb someday? ")

    # Store the responses in the dictionary.
    responses[name] = response # name as the key, response as the value

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

