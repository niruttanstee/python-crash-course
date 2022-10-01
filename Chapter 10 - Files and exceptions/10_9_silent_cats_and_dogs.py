# Modify the except block in last exercise to fail silently if either file is
# missing.


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
    # FAILING SILENTLY BY USING pass
    pass