# Make several dictionaries, where each dictionary represents a different
# pet. In each dictionary, include a kind of animal and the owner's name.
# Store these dictionaries in a list called pets. Next, loop through your list
# and as you do, print everything you know about the pet.

pet_0 = {
    'kind': 'dog',
    'owner_name': 'nirutt',
}
pet_1 = {
    'kind': 'cat',
    'owner_name': 'sandra',
}
pet_2 = {
    'kind': 'rabbit',
    'owner_name': 'ethan',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets: 
    print(f"Kind: {pet['kind'].title()}")
    print(f"\tOwner: {pet['owner_name'].title()}")

