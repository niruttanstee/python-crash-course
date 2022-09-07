# Store the user class in one module, and store the Privileges and Admin class
# in a separate module.

# In a separate file, create an Admin instance and call show_privileges() to
# show that everything is still working correctly.

from admin import Admin

new_admin = Admin('nirutt', 'anstee', 23)
new_admin.privileges.show_privileges()