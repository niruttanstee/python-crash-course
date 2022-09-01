# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the
# the function call provides, and it should print a summary of the sandwich
# that's being ordered. Call the function three times, using a different
# number of arguments each time.

def make_sandwich(*ingredients):
    """Prints a summary of the sandwich that's being ordered."""
    print("\nSandwich ingredients")
    for ingredient in ingredients:
        print(f"-   {ingredient}")

make_sandwich('chicken')
make_sandwich('tuna', 'sweetcorn', 'mayo')
make_sandwich('cheese', 'tomato', 'beef', 'lettuce', 'egg')