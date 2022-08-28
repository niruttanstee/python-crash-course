# Make an intentional error for lists by using the wrong index.
guests = ['Anna', 'Melissa', 'Alicia', 'Daisy']
# This will create an index out of range error as index starts at 0 not 1 and we are calling the 4th index which is nothing.
print(guests[4])