# Write a program that reads the learning_python.txt and prints what its
# written three times.

# Print the contents once by reading in the entire file, once by looping over
# the file object, and once by storing the lines in a list and then working
# with them outside the with block.

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines) # printing entire file
    print('\n')
    
    for line in lines:
        print(line.strip()) # looping over the file object
    print('\n')
    
    learnt_list = []
    for line in lines:
        learnt_list.append(line.strip())

for learnt in learnt_list:
    print(learnt)