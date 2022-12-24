from a11_3_employee import Employee
import unittest

class EmployeeTestCase(unittest.TestCase):
    """Tests Employee class."""

    # 5. Use setUp() method so you don't have to create a new employee
    # instance in each test method.
    def setUp(self):
        """
        Create employee class and a set custom raise attributes to test test_give_custom_raise() function.
        """
        self.nirutt = Employee('nirutt', 'anstee', 65_000)
    
    def test_give_default_raise(self):
        """Test give_raise() default raise work correctly."""
        self.nirutt.give_raise()
        self.assertEqual(self.nirutt.salary, 70_000)
    
    def test_give_custom_raise(self):
        """Test give_raise() with custom amount if it works correctly."""
        self.nirutt.give_raise(10000)
        self.assertEqual(self.nirutt.salary, 75_000)
    
if __name__ == '__main__':
    unittest.main()

# 6. Run the test case and make sure both tests pass.