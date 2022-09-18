# We can write a program that reads in the contents of a text file and rewrite
# it.

# Step 1 is to read the file into memory by reading the entire content or
# reading it one line at a time.

# To do any work on the file we need to open it using the open function needs
# one argument: the name of the file we want to open.

# Python then looks for the file in the directory where the program that's
# currently running. This then returns the object of the file so we use (as)
# we use the read() method in the second line of the program to read the
# entire contents, when we print the value of the content we get the contents
# of the file...

# The file seems to need the entire path. This is called the absolute file
# path.
file_path = "pi_digits.txt"

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)