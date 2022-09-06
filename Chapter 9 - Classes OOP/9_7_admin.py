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
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    # Write a method called show_privileges() that lists the administrator's set
    # of privileges. 
    def show_privileges(self):
        """Prints all admin privileges."""
        print("\n--- Admin privileges ---")
        for privilege in self.privileges:
            print(f"{privilege}")

# Create an instance of Admin and call your method.
an_admin = Admin('nirutt', 'anstee', 23)
an_admin.describe_user()
an_admin.show_privileges()