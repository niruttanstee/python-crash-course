# Modify the make_shirt() function so that shirts are large by default with a
# message that reads I love Python. Make a large shirt and a medium shirt 
# with the default message, and a shirt of any size with a different message.

def make_shirt(size="large", message="I love Python"):
    """Prints summarize of t-shirt size and message."""
    print(f"T-shirt of size {size} should be printed with {message}.")

# 1 make a large shirt with default message
make_shirt()

# 2 make a medium shirt with default message
make_shirt(size="medium")

# 3 Shirt of any size with different message
make_shirt("small", "Cool thing")