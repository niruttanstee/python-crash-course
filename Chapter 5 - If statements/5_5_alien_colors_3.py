# Making it an if-elif-else chain.
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
alien_test_list = ['green', 'yellow', 'red']

for alien in alien_test_list:
    if alien == 'green':
        points = 5
    elif alien == 'yellow':
        points = 10
    else:
        points = 15
    
    print(f"You earned: {points} points.")
