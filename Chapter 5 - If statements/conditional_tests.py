# Conditional tests of statement is an expression that can be evaluated as
# True or False. Python uses the conditional values to decide whether the code
# in the IF statement should be executed, if True it is executed otherwise,
# it is ignored.

# Checking for Equality (Operator ==) if value of left side and right side of
# the operator match
car = 'bmw'
print(car == 'bmw') # True
print(car == 'audi') # False

# A single = sign is a statement (Set the value of car equal to 'bmw')
# Checking equality is CASE SENSITIVE
car = 'Lexus'
print(car == 'lexus') # False
print(car.lower() == 'lexus') # True (If case doesn't matter)

# Checking for inequality by using the (!=) NOT operator
requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")