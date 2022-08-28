# This will demonstrate the for loop indentation error, Python will show you where an expected indent should be.
magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician) # This will create an error.

# This is an example of a LOGICAL ERROR because it's valid Python code but not the one we expect.
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait too see your next trick, {magician.title()}.\n")
# The above print statement is valid but will only be printed at the end for the last magician in the magicians list. 

# Colons are used to tell Python that the next line is nested to process inside a loop, without a colon Python will throw an error e.g.
# for magician in magicians <------
#    print(f"{magician.title()}, that was a great trick!")
