# Use a method to give a capital letter to each word e.g. such as in a string name and print it.
name = "ada lovelace"
name = name.title()
print(name)

# Use a method to give uppercase and lowercase to the string name and print it.
print(name.upper())
print(name.lower())

# Using f-strings (format strings) to compose a message
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)