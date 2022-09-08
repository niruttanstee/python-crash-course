from random import randint
# Make a class Die with one attribute called sides, which has a default
# value of 6.

class Die:
    """Simulates a dice with a custom number of sides."""
    
    def __init__(self, sides=6):
        """Initializes attribute for number of sides of the die."""
        self.sides = sides

    # Write a method called roll_die() that prints a random number between 1 and
    # the number of sides the die has.

    def roll_die(self):
        """
        Rolls the dice resulting in a number between 1 to the number of sides
        set.
        """
        die_result = randint(1, self.sides)
        print(f"{self.sides}-sided die, rolled: {die_result}")

# Make a 6-sided die and roll it 10 times.
def roll_ten_times(sides=6):
    """
    Calls the Die class 10 times to roll the dice with a set number of
    sides.
    """
    count = 0
    dice = Die(sides)
    while count < 10:
        dice.roll_die()
        count+= 1

roll_ten_times()