# an example of if statements of a car list. Finds the car with the correct
# value and then if found, the value is printed in uppercase, otherwise print
# car in title case.
cars = ['audi', 'mercedes', 'toyota', 'lexus']

for car in cars:
    if car == 'lexus':
        print(car.upper())
    else:
        print(car.title())