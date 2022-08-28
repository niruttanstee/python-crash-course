# The space needs to be reduced to 2 guests. 
guests = ['Anna', 'Melissa', 'Alicia', 'Daisy']
guests.insert(0, 'Rebecca')
guests.insert(2, 'Millie')
guests.append('Gal')

# Send a message to everyone to say that you can only invite two people for dinner.
print(f"{guests[0]}, I can only invite two people.")
print(f"{guests[1]}, I can only invite two people.")
print(f"{guests[2]}, I can only invite two people.")
print(f"{guests[3]}, I can only invite two people.")
print(f"{guests[4]}, I can only invite two people.")
print(f"{guests[5]}, I can only invite two people.")
print(f"{guests[6]}, I can only invite two people.")

# Use pop() to remove remove guests from the list one at a time only 2 guests remain. Each time a guest is popped, print a message letting them know you're sorry you can't invite them for dinner.
print(f"I'm sorry {guests.pop()} but I can't invite you to dinner.")
print(f"I'm sorry {guests.pop()} but I can't invite you to dinner.")
print(f"I'm sorry {guests.pop()} but I can't invite you to dinner.")
print(f"I'm sorry {guests.pop()} but I can't invite you to dinner.")
print(f"I'm sorry {guests.pop()} but I can't invite you to dinner.")

# Print a message to the two in the list letting them know they're still invited.
print(f"You're still invited though, {guests[0]}")
print(f"You're still invited though, {guests[1]}")

# Use del statement to remove the last names from the list and print an empty list.
del guests[1]
del guests[0]
print(guests)