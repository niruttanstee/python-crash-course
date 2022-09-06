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

# An administrator is a special kind or user. Write a class called Admin that
# inherits from the User class.

class Admin(User):
    """Simulates an admin user."""

    # Add an attribute, privileges, that stores a list of strings like
    # "can add post", "can delete post", "can ban user", and so on.
    def __init__(self, first_name, last_name, age):
        """Initializes the privilege and inherited attributes."""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

# Write a separate Privileges class.

# The class should have one attribute, privileges, that stores a list of
# strings described in admin.py.
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


# Create a new instance of Admin and use your method to show its privileges.
new_admin = Admin('nirutt', 'anstee', 23)
new_admin.describe_user()
new_admin.privileges.show_privileges()