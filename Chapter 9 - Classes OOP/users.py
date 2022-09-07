"""Module simulates"""
class User:
    """Simulates a user profile."""

    def __init__(self, first_name, last_name, age):
        """Initializes the user first name, last name, age and activeness."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.active = True
    
    def describe_user(self):
        """Prints a summary of the user."""
        print(f"\n--- User information ---")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Active?: {self.active}")
    
    def greet_user(self):
        """Greets the user to take their medicine."""
        print(f"\nHello {self.first_name}, please take your medicine!\n")

class Admin(User):
    """Simulates an admin user."""

    # Add an attribute, privileges, that stores a list of strings like
    # "can add post", "can delete post", "can ban user", and so on.
    def __init__(self, first_name, last_name, age):
        """Initializes the privilege and inherited attributes."""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

class Privileges():
    """Simulates a user privileges."""

    def __init__(self, 
        privileges=
            [
            'can add post', 
            'can delete post', 
            'can ban user'
            ]):
        """Initializes privileges list."""
        self.privileges = privileges

    # Move the show_privileges() method to this class. Make a Privileges 
    # instance as an attribute in the Admin class. 
    def show_privileges(self):
        """Prints all admin privileges."""
        print("\n--- Admin privileges ---")
        for privilege in self.privileges:
            print(f"{privilege}")