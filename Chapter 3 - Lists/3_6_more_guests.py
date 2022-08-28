# More people can now be invited to the dinner. Pick three more guests to invite.
guests = ['Anna', 'Melissa', 'Alicia', 'Daisy']

# Print to inform guests that you found a bigger dining table.
print(f"{guests[0]}, we've a bigger table so I'm going to invite more guests.")
print(f"{guests[1]}, we've a bigger table so I'm going to invite more guests.")
print(f"{guests[2]}, we've a bigger table so I'm going to invite more guests.")
print(f"{guests[3]}, we've a bigger table so I'm going to invite more guests.")

# Use insert() to add one new guest to the beginning of the list.
guests.insert(0, 'Rebecca')
print(guests)

# Use insert() to add one new guest to the middle of the list.
guests.insert(2, 'Millie')
print(guests)

# Use append() to add one new guest to the end of the list.
guests.append('Gal')
print(guests)

# Print a new set of invitation messages, one for each person in the list.
print(f"Madame {guests[0]}, I am inviting you to join me for dinner.")
print(f"Madame {guests[1]}, I am inviting you to join me for dinner.")
print(f"Madame {guests[2]}, I am inviting you to join me for dinner.")
print(f"Madame {guests[3]}, I am inviting you to join me for dinner.")
print(f"Madame {guests[4]}, I am inviting you to join me for dinner.")
print(f"Madame {guests[5]}, I am inviting you to join me for dinner.")
print(f"Madame {guests[6]}, I am inviting you to join me for dinner.")