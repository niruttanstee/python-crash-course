# We can modify attributes in class by creating a method inside that does it
# or directly.

# Let's a write a Car class representing a car.
# We can set a DEFAULT VALUE for an attribute


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

        

# sample value
my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# We can modify attribute value DIRECTLY
my_new_car.odometer_reading = 23 # setting this directly
print("\nAfter updating odometer directly...")
my_new_car.read_odometer()

# We can modify attribute through a method (see last method)
my_new_car.update_odometer(500)
print("\nAfter updating odometer directly...")
my_new_car.read_odometer()

# Check if odometer can be rolled back (it shouldn't)
my_new_car.update_odometer(10)

# Incrementing odometer by supplying a value
my_new_car.increment_odometer(1)
print("\nAfter incrementing odometer directly...")
my_new_car.read_odometer()