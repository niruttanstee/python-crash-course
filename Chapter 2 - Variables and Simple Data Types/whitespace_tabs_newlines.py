# Create whitespace to strings using tabs and newlines.
#   Tabs uses the format: \t
#   Newline uses the format: \n
print("\tPrint a tab")
print("\n")
print("Print a new line:\nThis is line 2\nThis is line 3")
print("\n")
print("Print both newline with an immediate tab:\n\tNew line Tab 1\n\tNew line Tab 2")

# Using a method to ensure that no whitespace exists on the right end of a string.
favorite_language = "python "
print(favorite_language)

print(favorite_language.rstrip()) 
# this only removes it for this very instance (temporarily) to remove the whitespace permanently we must associate the stripped value with the variable name. e.g
favorite_language = favorite_language.rstrip()
print(favorite_language)

# rstrip() == right strip whitespace
# lstrip() == left strip whitespace
# strip() == strip whitespace from both side