# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as One of my favorite books is
# Alive in Wonderland. Call the function, making sure to include a book title
# as an argument in the function call.

def favorite_book(title):
    """
    Prints a simple message with the title parameter.
    Param: title, string title of a book
    """
    print(f"One of my favorite books is {title}.")

favorite_book("Dune")