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

# Favorite languages scenario, we can allow people to choose multiple 
# languages instead of just one.

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite programming languages are:")
    for language in languages: # nesting a for loop inside another
        print(f"\t{language.title()}") 

# We should not nest too deeply (1 nested loop inside another is enough and 
# nesting dictionaries in lists or vice versa)
# as it becomes incredibly inefficient and complex.

# A dictionary in a dictionary.
# It can become complicated quickly so we need to plan it properly.
# Scenario, if we have several users for a website, each with a unique
# username, you can use the usernames as the keys in the dictionary. We can
# then store information about each user by using a dictionary as the value
# associated with their username i.e. first name, last name, and location.
users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mercury': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# When dictionaries are nested in another we must ensure that they are
# structured clearly and consistently, although each structure can be 
# different, it can become complicated.