# Using loops and if statements to check for special items.
# Checking for toppings that has ran out from list.
import re


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# Normal loop without check
for topping in requested_toppings:
    print(f"Adding {topping}.")

print("Finished making your pizza!")

# Loop with checking for item that ran out
for topping in requested_toppings:
    if topping == 'green peppers': #item that ran out
        print(f"Sorry we are out of {topping} right now.")
    else: # ensures that every other topping is processed
        print(f"Adding {topping}.")

print("Finished making your pizza!")