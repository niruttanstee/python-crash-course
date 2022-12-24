# Let's see what a failing test looks like. We'll create another function
# called get_formatted_name_and_middle() so it can handle middle names, but
# we'll do so in a way that breaks the function for names with just a first
# and last name, like Janis Joplin.

import unittest
from name_function import get_formatted_name_and_middle as fn

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_middle_last_name(self):
        """Do names like 'Janis Joplin' work?'"""
        formatted_name = fn('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()