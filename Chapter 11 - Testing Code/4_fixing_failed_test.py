# We'll make the name_function, get_formatted_name middle variable optional.
# By moving the the middle parameter to the end and giving it an empty default
# value. We also add an if statement to test if middle value is used or not.

# Let's test for Janis Joplin again.

import unittest
from name_function import get_formatted_name  as fn

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'.'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = fn('Janis', 'Joplin')
        self.assertEqual(formatted_name, "Janis Joplin")

    # we can add new tests to test cases where a middle name is inserted.
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = fn('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

if __name__ == "__main__":
    unittest.main()