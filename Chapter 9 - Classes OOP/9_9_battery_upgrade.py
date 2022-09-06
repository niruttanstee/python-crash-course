# Use the final version of the electric_car.py from this section.

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
class ElectricCar(Car): # To use parent we supply class Car as a parameter
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # get parameter from calling variable
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) # set argument from variable call to initialize parent class
        # using the keyword super().__init__()
        self.battery = Battery() # 1.

    # 1.
    def describe_battery(self):
        """Print a statement  describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # 2.
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks!"""
        print("This car does not need a gas tank!")

# Add a method to the battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 100 if it isn't
# already.
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

    def upgrade_battery(self):
        """Updates the battery capacity to 100 if it isn't already."""
        self.battery_size = 100

# Make an electric car with the default battery size, call get_range() once,
# and then get_range() the second time after upgrading the battery.
electric_car = ElectricCar('tesla', 'model s', 2022)
print(electric_car.get_descriptive_name())
electric_car.battery.describe_battery()
electric_car.battery.get_range()

# We should see an increase in the car's range.
electric_car.battery.upgrade_battery()
electric_car.battery.describe_battery()
electric_car.battery.get_range()