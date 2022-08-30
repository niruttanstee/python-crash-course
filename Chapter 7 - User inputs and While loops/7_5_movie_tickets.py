# A movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free; if they are between
# 3 and 12, the ticket is $10; and if they are over the age of 12, the ticket
# is $15. Write a loop in which you ask users their age, and then tell them
# the cost of their movie ticket.

prompt = "\nEnter your age to calculate the price for your ticket:"
prompt += "\nType 'quit' to exit the program. "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        price = "free"
    elif age >= 3 and age <= 12:
        price = "$10"
    else:
        price = "$15"
    
    print(f"The movie tickets costs: {price}.")