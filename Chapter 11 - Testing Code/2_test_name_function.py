# The syntax for creating a test case takes a little time to get used to.
# Once we create a test case it's straightforward to add more unit test for our
# functions. To write a test case for a function, we import unittest module
# and the function you want to test. Then create a class that inherits from
# unittest. TestCase, and write a series of methods to test different aspects
# of our function's behavior.

# Here's a test case with one method that verifies that the function
# get_formatted_name() works correctly when given the first and last name.

import unittest # 1. import unittest 
from name_function import get_formatted_name as fn # 2. import function to test

class NamesTestCase(unittest.TestCase): # create a class which will contain a series of unit tests for the function
    """Tests for 'name_function.py'.""" # class must inherit from the class unittest.TestCase 

    def test_first_last_name(self): # a method that tests one aspect of get_formatted_name function
        """Do names like 'Janis Joplin' work?""" # any method that has test_ at the start will run automatically
        formatted_name = fn('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') # assert method verifies that a result we receive matches the result
        # we posed to return i.e including capitalization. 


# The if block looks at a special variable __name__ which is set when the program is executed. 
# If the file is being run as the main program, the value of __name__ is set to '__main__'.
# In this case, we call unittest.main() which runs the test case.

# When a testing framework import this file, the value of __name__ won't be '__main__'.
# This block will not be executed.
if __name__ == '__main__':
    unittest.main()

