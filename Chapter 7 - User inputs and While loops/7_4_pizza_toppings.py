# Write a loop that prompts the user to enter a series of pizza toppings until
# they enter a 'quit' value. As they enter each topping, print a message
# saying you'll add the topping to their pizza.

prompt = "\nEnter your pizza toppings, so I can make your pizza:"
prompt += "\nType 'quit' to exit the program. "


while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"Added {topping} to your pizza.")