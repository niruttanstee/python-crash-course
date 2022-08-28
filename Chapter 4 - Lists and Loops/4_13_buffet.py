# A buffet style restaurant only offer five basic foods, think of simple foods and store them in a tuple.
buffet_foods = ('chicken wings', 'spare ribs', 'rice', 'chocolate cake', 'stir-fry chicken')
# 1. Use a for loop to print each food the restaurant offers.
print("Here are the five buffet foods:")
for food in buffet_foods:
    print(food)

# 2. Try to modify one of the items, and make sure that Python rejects the change.
# buffet_foods[1] = 'pasta'

# 3. The restaurant changes its menu, replacing two of the items with different foods. Add a line that
# rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
buffet_foods = ('chicken wings', 'spare ribs', 'chicken nuggets', 'burger', 'chocolate cake')
print("\nThe new and updated food:")
for food in buffet_foods:
    print(food)
