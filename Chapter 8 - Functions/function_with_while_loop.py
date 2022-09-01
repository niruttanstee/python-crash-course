# We can use functions with all the Python structures you've learned about so
# far. For example, let's use the get_formatted_name() function with a while
# loop to greet users more formally.

def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' anytime to quit)")
    f_name = input("First name: ") 
    if f_name == 'q': # Add a way to stop the loop.
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(first_name=f_name, last_name=l_name)
    print(f"\nHello, {formatted_name}")


