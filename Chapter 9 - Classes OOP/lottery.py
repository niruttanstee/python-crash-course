from random import choice

"""Module simulates a lottery draw."""

class Lottery:
    """Simulates a lottery though draw functions."""

    def __init__(self):
        """Initializes the available lottery numbers."""
        self.lottery_numbers = (
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                'a', 'b', 'c', 'd', 'e'
        )

    def draw(self):
        """Draws the lottery from available numbers."""
        lottery_result = []
        count = 0

        while count < 6:
            selected_number = choice(self.lottery_numbers)
            lottery_result.append(selected_number)
            # Don't forget this
            count += 1

        # Strip any leading or trailing whitespaces
        return lottery_result