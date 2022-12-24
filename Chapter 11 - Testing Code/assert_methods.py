# Python provides a number of assert methods in the unittest.TestCase class.

# Asset methods test whether a condition you believe is true at a specific 
# point in your code is indeed true.

# Here are the six commonly used assert methods.
import unittest 

class AssertTestCase(unittest.TestCase):
    """Class with six commonly used assert methods."""

    def __init__(self):
        a, b, x, item = 0
        
        self.assertEqual(a, b) # Verify that a == b
        self.assertNotEqual(a, b) # Verify that a != b
        self.assertTrue(x) # Verify that x is True
        self.assertFalse(x) # Verify that x is False
        self.assertIn(item, list) # Verify that item is in list
        self.assertNotIn(item, list) # Verify that item is not in list
        
    