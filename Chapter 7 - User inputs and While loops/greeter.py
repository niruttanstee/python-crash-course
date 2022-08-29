# Tell the user what to enter makes it easy for both the user and programmer.
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# Sometimes you'll need to write a prompt that's longer than the one line.
# For example, you might want to tell the user why you're asking for certain
# input. 

# Assign the prompt to a variable and pass that variable to the input()
# function. Building the prompt over several lines, then write a clean
# return statement.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? " # You can use += to add like int var.

name = input(prompt)
print(f"\nHello, {name}!")