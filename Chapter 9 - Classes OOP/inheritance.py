# INHERITANCE
# We don't need to start from scratch when writing a class. If the class we're
# writing is a specialized version of another class we wrote, we can just
# inherit from it.

# It takes on the attributes and methods of the first class. The original class
# is called the PARENT class, and the new class is the CHILD class.

# The child can inherit all or any attributes from the parent class, but it's
# also free to define new attributes and methods of its own.

# We must call the parent class using __init__ method in the child class.
# This will initialise any attributes defined in the parent class for the
# child class. 

# Example, let's model an electric car. An electric car is just a specific
# kind of car, so we can base our new ElectricCar class on the Car class
# we wrote earlier.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initializes attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Default value

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Function that updates the odometer value
    # We'll also add some additional code to prevent odometer reading rollback.
    def update_odometer(self, mileage):
        """
        Sets the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # Let's add a function to increment the odometer i.e. when a car is driven
    # the odometer should increase.
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# The CHILD CLASS
class ElectricCar(Car): # To use parent we supply class Car as a parameter
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # get parameter from calling variable
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) # set argument from variable call to initialize parent class
        # using the keyword super().__init__()
        self.battery_size = 75 # 1.

    # 1.
    def describe_battery(self):
        """Print a statement  describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # 2.
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks!"""
        print("This car does not need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# The super() function is a special function that allows us to all a method
# from the parent class. It tells for this instance to call the parent's
# init method from Car, which gives ElectricCar instance all the attributes
# defined in that method. The name super comes from a convention of calling
# the parent class a superclass and the child class a subclass.
 
# 1. We can also add attributes and methods to the child class and not affect
# the parent class.

# 2. We can OVERRIDE methods from the parent class if it doesn't fit with the
# child class. We define a method in the child class with the same name of the
# method in the parent class we want to change. Python will disregard the
# parent's class and only pay attention to the method in the child class.
# I.e or electric cars, the class Car has a method called fill_gas_tank()
my_tesla.fill_gas_tank() 