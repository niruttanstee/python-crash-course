# Lists are created using square brackets with elements seperated by commas.
bicycles = ['trek', 'cannondale', 'redlines', 'specialized']

# This will print the entirety of the list in its brackets.
print(bicycles)

# Lists are ordered collections therefore we can tell Python to show an element by using the position or the "index".
print(bicycles[0])

# We can format the element string.
print(bicycles[0].title())

# Index position starts at 0 NOT 1
# Get the last item in the list, in Python we can use index -1.
print(bicycles[-1])

# Get the nth last item in the list, in Python we can use index -n.
print(bicycles[-3]) # print the 3rd last element.

# Using values from a list to compose a message.
message = f"My first bicycle was a {bicycles[1].title()}."
print(message)