# Working with file's contents
# After we've read a file into memory, we can do whatever we want with that
# data.
# In this scenario we will print he pi in one single line as a string.

from copyreg import pickle


filename = 'pi_digits.txt'

with open(filename) as file_objects:
    lines = file_objects.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string) # prints the pi string in one line
print(len(pi_string)) # prints the number of letters in pi string

# ONE MILLION DIGITS
# We can work work much larger files for example a file with pi of 1m digits.
# Instead of printing 1m digits we can print the first 50 decimals in the
# terminal.

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:52]}...")
print(len(pi_string))