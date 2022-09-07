# Start with the work from User, Admin and Privileges. Store them into one
# module.

from users import Admin

# Make an Admin instance, and call show_privileges() to show everything is
# working correctly.

an_admin = Admin('nirutt', 'anstee', 23)
an_admin.privileges.show_privileges()

