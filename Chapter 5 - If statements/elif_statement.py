# Amusement park admission for multiple age groups.
import re


age = 12
# Admission for anyone under 4 is free.
# Admission for anyone between the ages of 4 and 18 is $25.
# Admission for anyone aged 18 and older is $40.
if age < 4:
    print("Your admission cost is $0.")
elif age < 18: # We don't need lower margin statement because the statement above will take place before if age is <4 so it won't reach this.
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# A better way
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")
# Note that the else block is OPTIONAL - it's a catchall statement and can
# include invalid or even malicious data.

# This is an efficient way to write code as it will catch most occurrences
# before the else statement so if its caught by an elif statement the rest of
# the block does not have to run.

# HOWEVER, sometimes we need to simply use multiple separate condition
# statements i.e for when we require to check all conditions of interests.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.") # This is never printed as there is no p... in list
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("Your pizza is ready.")



