# Start with your program from exercise 9_1.
# Add an attribute called number_served with a default value of 0.

class Restaurant:
    """A class that simulates a restaurant with a name and cuisine type."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints a simple description of restaurant attributes."""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Restaurant cuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Prints a simple message saying that the restaurant is open."""
        print("The restaurant is open!")

    def set_number_served(self, number_served):
        """Set the number of customers served at the restaurant."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment the number of customers served by a supplied number."""
        self.number_served += number_served

# Create an instance called restaurant from this class.
restaurant = Restaurant('wagamamas', 'japanese')

# Print the numbers of customers the restaurant has served, and then change 
# this value and print it again.
print(restaurant.number_served)
restaurant.number_served = 20
print(restaurant.number_served)


# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and
# print the value again.
restaurant.set_number_served(10)
print(restaurant.number_served)


# Add a method called increment_number_served() that lets you increment the
# number of customers who've been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.
restaurant.increment_number_served(30)
print(restaurant.number_served)