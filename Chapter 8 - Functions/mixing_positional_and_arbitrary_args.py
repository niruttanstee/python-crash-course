# Mixing positional and arbitrary arguments.
# The parameter that takes arbitrary arguments must be placed last in the
# function definition.
# 
# Python matches positional argument and keyword arguments first and then
# collects any remaining arguments in the final parameter.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}") 

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# You'll see the generic parameter name *args, which collects arbitrary
# positional arguments like this.å 