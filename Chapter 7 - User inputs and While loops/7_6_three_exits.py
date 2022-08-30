# Modify the program that does the following at least once.
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nEnter your age to calculate the price for your ticket:"
prompt += "\nType 'quit' to exit the program. "

# Using a conditional test in the while statement to stop the loop.
# age = ""
# while age != 'quit':
#     age = input(prompt)
#     if age == 'quit':
#         continue
#     age = int(age)

#     if age < 3:
#         price = "free"
#     elif age >= 3 and age <= 12:
#         price = "$10"
#     else:
#         price = "$15"
    
#     print(f"The movie tickets costs: {price}.")


# Use an active variable to control how long the loop runs.
status = True
while status:
    age = input(prompt)
    if age != 'quit':
        age = int(age)

        if age < 3:
            price = "free"
        elif age >= 3 and age <= 12:
            price = "$10"
        else:
            price = "$15"
        
        print(f"The movie tickets costs: {price}.")
    else:
        status = False



# Using a break statement.
# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break

#     age = int(age)

#     if age < 3:
#         price = "free"
#     elif age >= 3 and age <= 12:
#         price = "$10"
#     else:
#         price = "$15"
    
#     print(f"The movie tickets costs: {price}.")