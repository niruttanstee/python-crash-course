# The write() function doesn't add any newlines to the text we write.
# So if we write more than one line without including newline characters,
# your file may not look the way you want in to:

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.")