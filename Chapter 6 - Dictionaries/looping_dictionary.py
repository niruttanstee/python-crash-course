# Looping through a dictionary of key-value paris. Scenario, a dictionary 
# storing information about a user on a website.
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
# Looping through all key-value pairs. Using a for loop. Remember the .items()
for key, value in user_0.items(): # Create names of two variables (k, v)
    # items() returns the list of key-value pairs.
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print(f"\n")


# Looping through all the KEYS in a dictionary. Using .keys() method.
# Good for when you don't need to work with values in the dictionary.
for key in user_0.keys():
    print(key.title())

print(f"\n")
# By default looping through keys is standard without needing a .keys().
# It's just the matter of readability.
for key in user_0:
    print(key.title())

print(f"\n")

# Some slightly more use cases.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!") #\t tab

# We can also check for someone not in the list.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take out poll!")

# Looping through dictionary keys in a particular order using sort()
print(f"\n")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# Looping through all VALUES in a dictionary.
# Using the .values()
print(f"\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Using set() method to not induce duplicates. Builds and returns a set.
# A set cannot contain duplicates elements.
print(f"\n")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
