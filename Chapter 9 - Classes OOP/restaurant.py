"""A module simulating a restaurant."""
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