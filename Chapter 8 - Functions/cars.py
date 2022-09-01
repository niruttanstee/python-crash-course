# Function to be imported for challenge.
def make_car(manufacturer, model_name, **car):
    """Returns a dictionary of a car information."""
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    return car