# Handling the FileNotFound Exception
# A common issue when working with files is handling missing files. The file
# we're looking for might be in a different location, the filename may be
# misspelled etc. 

# Let's try to read the file that does not exist:
filename = 'alice.txt'

# In this example the open() function produces the error, so to handle it, the
# try block will begin with the line that contains open():
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read() # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")