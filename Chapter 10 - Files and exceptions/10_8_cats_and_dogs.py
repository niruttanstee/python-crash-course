# Make two files, cats.txt and dogs.txt.
# Store at least three names of cats in the first files and print the contents
# of the file to the screen. Wrap the code in a try-except block to catch
# the FileNotFound error, and print a friendly message if a file is missing.

# Move one of the files to a different location on your system, and make sure
# the code in the except block executes properly.

cat_path = '/Users/nirutt/Documents/Code/python/crash_course/python-crash-course/Chapter 10 - Files and exceptions/text-files/cats.txt'
dog_path = '/Users/nirutt/Documents/Code/python/crash_course/python-crash-course/Chapter 10 - Files and exceptions/text-files/dogs.txt'

try:
    # print cat.txt
    print("Cat.txt")
    with open(cat_path) as f:
        names = f.read()
        print(names)
    # print dog.txt
    print("\nDog.txt")
    with open(dog_path) as f:
        names = f.read()
        print(names)
except FileNotFoundError:
    print(f"File does not exist in this path")