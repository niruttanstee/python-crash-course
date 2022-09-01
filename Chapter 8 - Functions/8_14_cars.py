# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.

# Call the function with the required information and two other name-value
# pairs, such as a color or an optional feature. Your function should work for
# a call like this one: 

# car = make_car('subaru', 'outback', color = 'blue', tow_package = True)

def make_car(manufacturer, model_name, **car):
    """Returns a dictionary of a car information."""
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    return car

car_0 = make_car('subaru', 'outback', color = 'blue', tow_package = True)
car_1 = make_car('aston martin', 'super car', color = 'racing green', tow_package = False)
print(car_0)
print(car_1)