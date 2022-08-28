# We can print the entire list of magicians using a for loop. This helps avoid problems in trying to print all the elements such as finding the index and makes code shorter.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# For each interval of loop Python is associating magician variable with each item in the magicians list. 

# Print a message to every magician to tell them, that they performed a great trick.
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    
# Adding a second line to the message to tell the magician that we're looking forward to their next trick.
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait too see your next trick, {magician.title()}.\n")
    
# Block of code that executes after the loop are those that aren't nested inside the loop.    
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait too see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")