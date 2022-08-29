# Sometimes we want to store multiple dictionaries in a list, or a list of
# multiple items in a dictionary. This is called NESTING. You can nest a list
# inside a list or a dictionary inside a dictionary also.

# A list of dictionaries - in storing a fleet of aliens.
# One way is to make a list of aliens in which each alien is a dictionary of
# information about that alien. The list is the fleet.

from hashlib import new


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens  = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Realistically we'd need more than 3 aliens with code that automatically 
# generates each alien. We can use the range() method to create a fleet of 30.

# Empty list for storing aliens.
aliens_0 = []

# Make 30 green aliens.
for alien_number in range(30): # 0 - 29 range alien number is the index
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens_0.append(new_alien)

# Show the first 5 aliens.
for alien in aliens_0[:5]: # first 5 ([5:] last 5)
    print(alien)
print("...")

# Show the number of aliens have been created.
print(f"Total number of aliens created: {len(aliens_0)}") # len() method

# Even though the aliens are identical Python detects it as individual objects
# in the list.

# We can modify the first few aliens by changing its characteristics. Like in 
# a game.
for alien in aliens_0[:3]:
    if alien['color'] == 'green': # checker
        alien['color'] = 'yellow' # modifier
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens_0[:5]:
    print(alien)
print("...")


# A list in a dictionary.
# Describing a pizza that someone is ordering. In this example two kinds of 
# information are stored for each pizza: a type of crust and a list of
# toppings. keys = crust, toppings.
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following " + 
    "toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")