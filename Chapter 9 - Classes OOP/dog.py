# A class Dog that represents any dog.
# We'll also write similarities of dogs to initialise the class.
# The properties of every dog is its name and age. Tells how to create an
# a Dog class representing a dog. 

# Capitalized name represents a class in Python
class Dog:
    """A simple attempt to model a dog."""

    # Initialize to create a class with properties name and age of dog.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Making an Instance from a Class
my_dog = Dog('Willie', 6)

# Call it like a function
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# The init method is automatically called to create the object Dog with the
# properties from the argument supplied of 'Willie' and 6, it then creates the
# instance representing this particular dog and sets the name and age
# attributes using the values provided.

# We can access ATTRIBUTES by simply calling the functions within using dot
# notation so my_dog.name gets the name of the dog in this class. 

# We can also call other functions in the class such as sit() and roll_over().
# To call functions we need to have double brackets, to call and get attributes
# we don't need the brackets.
my_dog.sit()
my_dog.roll_over()

# We can create MULTIPLE INSTANCES
dog_0 = Dog('James', 4)
dog_1 = Dog('Jennifer Lopez', 1)

print(f"My dog's name is {dog_0.name}.")
print(f"My dog is {dog_0.age} years old.")
print(f"My dog's name is {dog_1.name}.")
print(f"My dog is {dog_1.age} years old.")

