# Using a program you wrote that has one function in it, store that function
# in a separate file. Import the function into your main program file, and call
# the function using each of these approaches:

from cars import make_car as mc

car = mc("lexus", "RH450", color='blue', drive='fwd')

print(car)