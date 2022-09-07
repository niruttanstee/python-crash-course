# Using the latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant.
from restaurant import Restaurant

# Make a Restaurant instance, and call one of the Restaurant's methods to
# show that the import statement is working properly.

wagamamas = Restaurant('wagamamas', 'japanese')
wagamamas.describe_restaurant()