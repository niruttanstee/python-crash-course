# Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order,
# such as I made your tuna sandwich. As each sandwich have been made, move it
# to the finished sandwiches list then print a message listing each sandwich 
# that was made.

sandwich_orders = ['blt', 'chicken and gam', 'tuna sweetcorn', 'prawn mayo']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print(f"\n--- All sandwiches made ---")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")

