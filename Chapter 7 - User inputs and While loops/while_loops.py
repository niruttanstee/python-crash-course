# for loop takes a collection of items and executes a block of code once for
# each item in the collection. In contrast, a while loop runs as long as, or
# WHILE, a certain condition is true.

# Making a counter to count from 1 to 5, stopping when the count reaches 5.

current_number = 1
while current_number <= 5: # loop as long as the condition is true
    print(current_number)
    current_number += 1 # increment number or an infinite loop will occur

# Most real life scenario is likely to contain while loops. For example, a 
# game needs a while loop to keep running as long as you want to keep playing,
# and so it can stop running as soon as you ask it to quit.

# Example, letting the user choose when to quit.
# Using inputs in a while loop to allow user to quit.
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = "" # empty string for input value

while message != 'quit': # while message is not quit, repeat block of code
    message = input(prompt)

    if message != 'quit':
        print(f"{message}")
