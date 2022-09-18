# When we are reading a file, we'll often want to examine each line of the
# file. We may want to read or look for certain information in the file or
# modify the text in the file in some way.

# We can use a for loop on the file object to examine each line from a file
# one line at a time:

filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)

print("\n")

# there is a blank line for every print line because there is an invisible
# newline character at the end of each line in the text file. To eliminate
# it we can use the rstrip() which eliminates the blank lines from the right.
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())