# Checking a value is NOT in list.
# The keyword is NOT in.
# e.g. banned users, check that the user is is not in the banned list to allow
# them access to something.
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")