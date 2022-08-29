# When you use the input() function, Python interprets everything the user
# enters as a string. To accept integers we can convert the string into
# an integer value by using int() function.

age = input("How old are you? (Enter a number): ")
age = int(age)
print(age >= 18)