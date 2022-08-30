# Using the list sandwich_orders, make sure the sandwich 'pastrami' appears in
# the list at least three times.
# 
# Add code near beginning of the program to print a message saying the deli
# has run out of pastrami, and then use a while loop to remove all occurrences
# of 'pastrami' from sandwiches_orders.
# 
# Then move all sandwiches in into finished sandwiches order.  

sandwich_orders = [
    'blt',
    'pastrami',
    'chicken and gam',
    'pastrami',
    'tuna sweetcorn',
    'prawn mayo',
    'pastrami'
]
finished_sandwiches = []

no_sandwich = 'pastrami'

print(f"The deli has run out of {no_sandwich}.")

while no_sandwich in sandwich_orders:
    sandwich_orders.remove(no_sandwich)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print(f"\n--- All sandwiches made ---")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")

