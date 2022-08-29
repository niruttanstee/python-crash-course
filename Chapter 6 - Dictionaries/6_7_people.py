# Make two new dictionaries representing different people, and store all
# three dictionaries in a list called people. Loop through your list of people.
# As you loop through the list, print everything you know about each person.
person_0 = {
    'first_name': 'nadine',
    'last_name': 'kisselstein',
    'age': 25,
    'city': 'frankfurt'
}
person_1 = {
    'first_name': 'nirutt',
    'last_name': 'anstee',
    'age': 23,
    'city': 'eastbourne'
}
person_2 = {
    'first_name': 'ethan',
    'last_name': 'phillips',
    'age': 23,
    'city': 'battle'
}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name.title()} is {person['age']} and lives in "
    + f"{person['city'].title()}.")