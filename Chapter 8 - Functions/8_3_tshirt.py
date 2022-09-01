# Write a function called make_shirt() that accepts a size and the text of a 
# message that that should be printed on the shirt. The function should print a
# sentence summarizing the size of the shirt and the message printed on it.

# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

def make_shirt(size, message):
    """Prints a summarize message of the size and message of the shirt."""
    print(f"The t-shirt is sized {size} with a message printed of {message}.")

make_shirt("small", "Simply de best") # Positional
make_shirt(message="Too cool", size="large") # Keyword