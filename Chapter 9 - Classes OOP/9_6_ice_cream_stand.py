# An ice cream stand is a specific kind of restaurant. Write a class
# called IceCreamStand that inherits from the restaurant class we wrote
# earlier.

class Restaurant:
    """A class that simulates a restaurant with a name and cuisine type."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a simple description of restaurant attributes."""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Restaurant cuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Prints a simple message saying that the restaurant is open."""
        print("The restaurant is open!")

class IceCreamStand(Restaurant):
    """Simulates an ice cream stand."""
    # Add an attribute called flavors that stores a list of ice cream flavors.
    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the ice cream stand class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'lemon']

    # Write a method that displays these flavors.
    def display_flavors(self):
        """Prints all the available flavors."""
        print("All the flavors available.")
        for flavor in self.flavors:
            print(f"{flavor.title()}")


# Create an instance of IceCreamStand, and call this method
ice_cream_stand = IceCreamStand('The ice place', 'ice cream')
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()