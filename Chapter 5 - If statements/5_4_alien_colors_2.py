# Choose a color for an alien as you did in exercise 5_3 and write an if-else
# chain.

alien_test_list = ['green', 'yellow', 'red']

# If the alien's color is green, print a statement that the player just earned
# 5 points for shooting the alien.

# If the alien's color isn't green, print a statement that the player just
# earned 10 points.

# Write one version of this program that runs the if block and another that
# runs the else block. * I did one that runs for all three tests.

for alien in alien_test_list:
    if alien == 'green':
        print("You just earned 5 points for shooting the alien!")
    else:
        print("You just earned 10 points.")
        