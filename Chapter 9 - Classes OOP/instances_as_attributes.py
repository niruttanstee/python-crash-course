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

# INSTANCES AS ATTRIBUTES
# When modelling something from the real world in code, you may find that
# you're adding more and more detail to a class. We may recognize that part
# of one class can be written as a separate class. Breaking it into smaller
# classes work really well. An example is we can create a battery class that
# works with all electric cars, as a separate non related class.

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # 5.
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on full charge.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() # calling a class and initializing battery.

# We create an electric car and assign it to the variable my_tesla. When we
# want to describe the battery, we need to work through the car's battery
# attribute.

my_tesla = ElectricCar('Tesla', 'Model S', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Calling a class within a class its like calling a function in a function.
# Just use DOT notation.

# 5. We'll add some extra features to the battery class. As now its in a
# separate class, to prevent cluttering the electric car class.
my_tesla.battery.get_range()


# THERE ARE NO WRONG ANSWERS
# Some classes may be necessary to portray an aspect of an object but there
# can be multiple ways to display it.