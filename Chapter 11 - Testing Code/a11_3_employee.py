# 1. Write a class called Employee.

# 2. The __init__() method should take in a first name, last name, and an
# an annual salary. Store each of these as attributes.

class Employee():
    """Gives annual salary to employee."""

    def __init__(self, firstname, lastname, salary):
        """Stores firstname, lastname and annual salary."""
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.salary = salary

    # 3. Write a method called give_raise() that adds $5,000 to the annual
    # salary by default but also accepts a different raise amount.
    def give_raise(self, amount=5000):
        """Gives $5,000 by default or a different amount."""
        self.salary += amount

# 4. Write a test case for Employee. Write two test methods,
# test_give_default_raise() and test_give_custom_raise().


# 5. Use setUp() method so you don't have to create a new employee
# instance in each test method.

# 6. Run the test case and make sure both tests pass.