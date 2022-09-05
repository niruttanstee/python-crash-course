# Add an attribute called login_attempts to your User class.

# Write a method called increment_login_attempts() that increments the value of
# login_attempts by 1.

# Write another method called reset_login_attempts() that resets the value of
# login_attempts to 0.

class User:
    """Simulates a user profile."""

    def __init__(self, first_name, last_name, age):
        """Initializes the user first name, last name, age and activeness."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.active = True
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints a summary of the user."""
        print(f"\n--- User information ---")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Active?: {self.active}")
    
    def greet_user(self):
        """Greets the user to take their medicine."""
        print(f"\nHello {self.first_name}, please take your medicine!\n")

    def increment_login_attempts(self):
        """Increments login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempts = 0

# Make an instance of the User class and call increment_login_attempts()
# several times. 
user = User('nirutt', 'anstee', 23)

increment = 0
while increment < 5:
    user.increment_login_attempts()
    increment += 1

# Print the value of login_attempts to make sure it was incremented properly,
# and then call reset_login_attempts(). Print login_attempts again to make
# sure it was reset to 0.
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
