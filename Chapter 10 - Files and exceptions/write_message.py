# We can save data to a file by writing text, the output will still be 
# available after we close the terminal containing the program's output.
# We can examine the output after a program finishes running, and we can share
# the output files with others as well.

# Writing to an empty file

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")

# Python on writes strings to a text file so if we have numerical values we
# need to convert them first.
