from car import Car
from battery import Battery

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