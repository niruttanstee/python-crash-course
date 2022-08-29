# A simple dictionary.
# A game featuring aliens that can have different colors and point values.
# A dictionary that stores information about a particular alien:

# Dictionary uses curly brackets with key : value pairs
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Keys can be any value, even a list or another dictionary

# Accessing values in a dictionary
# e.g. if the player shoots down this alien, we can get the points to add to
# the user.
new_points  = alien_0['points'] # returns the value associated with key
print(f"You just earned {new_points} points!")

# Adding new key value pairs
# Give name of dictionary followed by the new key in square brackets along
# with new values.
# e.g adding x and y coordinates to aliens.
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# Starting with an empty dictionary is quite common
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

# Modifying values in a dictionary
# Give the name of the dictionary with the key which value must change in 
# square brackets and then the new value
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# A more interesting example we can track the position of an alien that move
# at different speeds.
# We'll store a value representing the alien's current speed and then use it
# to determine how far to the right the alien should move.
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_2['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}")

# Removing key value pairs.
# We can use the del statement to remove a key value pair. 
print(alien_0)
del alien_0['points'] # delete
print(alien_0)