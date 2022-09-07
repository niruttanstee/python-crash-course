# Importing classes

# 1. Importing a SINGLE CLASS
# First we'll create a module containing just the Car class, car.py.
# Every module requires a docstring

from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# We import the class Car, remember to put the first letter as uppercase. 

# 2. Storing MULTIPLE CLASSES in a module
# We can call other classes in the module, we don't have to import all of the
# classes for child and parent classes to work.

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# 3. Importing multiple classes from a module
# We can do that just like importing functions, use commas. 

from car import Car, ElectricCar


# 4. Importing an entire module
# After that we can then access the classes we need using dot notations.
# Because every call that creates an instance of a class includes the
# module names, you won't have naming conflicts with any names used in the
# current file. 

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_new_tesla = car.ElectricCar('tesla', 'model y', 2020)
print(my_new_tesla.get_descriptive_name())


# 5. Importing all classes from a module
# We can import every class from a module using the following syntax:

# from module_name import *

# This method is not recommended as it's clearer to to label the classes on
# the get go, its unclear which class we're using in the module. Lead to
# confusion with names in the file. Names can overlap each other.

# 6. Importing a module into a module
# Sometimes a class can be complex and large, we can split all classes into
# individual modules and import only ones that relates to that module.

from car import Car
from electric_car import ElectricCar

# 7. We can use alias to rename classes clearer.

from electric_car import ElectricCar as EC

tesla_1 = EC('tesla', 'roadster', 2019)
print(tesla_1.get_descriptive_name())
tesla_1.battery.describe_battery()