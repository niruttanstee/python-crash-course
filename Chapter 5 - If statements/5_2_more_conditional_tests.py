# More conditional tests to get the hang of it.

# Test for equality and in equality with strings.
os_tuple = ('linux', 'macos', 'windows')
if os_tuple[0] == 'linux':
    print("Linux is in the list")
if os_tuple[2] == 'arch linux':
    print("Arch Linux is in 3rd place")

# Tests using the lower() method
a_word = 'ChiCken'
print(a_word == 'chicken') # False
print(a_word.lower() == 'chicken') # True

# Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to.
a_number = 555
print(f"555 is equal to {a_number}? {555 == a_number}") # equality
print(f"500 is equal to {a_number}? {500 == a_number}") # inequality
print(f"400 is greater than {a_number}? {400 > a_number}") # greater than
print(f"400 is less than {a_number}? {400 < a_number}") # less than

# using and / or keyword
print(a_number >= 554 and a_number <= 600) # True
print(a_number >= 554 or a_number <= 100) # True

# Test whether item is in a list
an_os = 'ios'
another_os = 'windoWs'
print(f"Is iOS in this list? {an_os in os_tuple}")
print(f"Is Windows in this list? {another_os.lower() in os_tuple}")

