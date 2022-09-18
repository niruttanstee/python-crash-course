# Appending to a file
# If we want to add content to a file instead of writing over existing content
# we can open the file in APPEND MODE (a), when we do this Python doesn't
# erase the contents of the file before returning the file object. Any lines
# we write will be added to the end of the file, if the file doesn't exist yet
# Python will create an empty file for us.

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")