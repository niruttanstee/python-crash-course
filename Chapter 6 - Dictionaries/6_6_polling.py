# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['sarah', 'nadine', 'phil', 'edward', 'master']

# Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
for key in favorite_languages:
    if key in people:
        print(f"{key.title()}, thank you for responding to the poll.")
    else:
        print(f"{key.title()}, please take the poll.")
