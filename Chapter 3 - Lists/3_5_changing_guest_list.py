# One of the guest can't make the dinner, so you need to send out a new set of invitations, by thinking of someone else to invite. 

# Use the previous list from 3_4.
guests = ['anna', 'melissa', 'alicia', 'daisy']
not_attending = 'daisy'
print(f"{not_attending.title()} can't make it to the dinner.")
guests[3] = 'rebecca'
print(f"Hey {guests[0].title()}, would you like to have dinner tonight?")
print(f"Hey {guests[1].title()}, would you like to have dinner tonight?")
print(f"Hey {guests[2].title()}, would you like to have dinner tonight?")
print(f"Hey {guests[3].title()}, would you like to have dinner tonight?")