# Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically stored
# in a user profile.

# Make a method called describe_user() that prints a summary of the user's
# information. Make another method called greet_user() that prints a
# personalized greeting to the user.

# Create several instances representing different users, and call both methods
# for each user.

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

# create several instances
user_0 = User('Nirutt', 'Anstee', 23)
user_1 = User('Nadine', 'Jackson', 30)
user_2 = User('Joom', 'Heisenberg', 40)

# call methods
user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()