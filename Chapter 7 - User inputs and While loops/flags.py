# In complex programs.
# When many different events could cause the program to stop running.
# Example, in a game, several different events can end the game. When the
# player runs out of ships, their time runs out, or the cities they were
# supposed to protect are all destroyed, the game should end.
# Testing and checking for when the game should end in one while statement
# becomes complicated and difficult.

# We can define one variable that determines whether or not the entire
# program is active. This variable called a FLAG, acts as a signal to the
# program.

# The flag can be set to true while active and stop running the while
# statement and several events can set the flag to false, thus out while
# statement only needs to check one condition, the flag.

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)