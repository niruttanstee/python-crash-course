# Checking a list is empty. We cannot assume that a list has at least an item
# in it, but in reality at times we may have empty list.

# i.e if a user wants a plain pizza.
requested_toppings = []

if requested_toppings: # if list is not empty (an empty list = False, 0)
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")