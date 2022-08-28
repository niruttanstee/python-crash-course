# Create a list of pizzas and then use a for loop to print the name of each pizza.
pizzas = ['pepperoni', 'edna', 'fungi']

# 1. Make a copy of the pizzas list and call it friend_pizzas
friend_pizzas = pizzas[:]

# 2. Add a new pizza to the the original list
pizzas.append('bbq chicken')

# 3. Add a different pizza to the list friend_pizzas
friend_pizzas.append('pineapple')

# 4. Prove that the lists are different
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)