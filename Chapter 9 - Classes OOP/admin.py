from users import User

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