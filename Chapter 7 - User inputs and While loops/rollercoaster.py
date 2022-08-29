# Consider a program that determines whether people are tall enough to ride
# a roller coaster:
height = input("How tall are you, in centimeters (cm)?: ")
height = int(height)

if height >= 150:
    print("\nYou're tall enough to ride!")
else:
    print("\nSorry, for your safety we cannot let you ride.")

# For any numerical comparisons always remember to convert the input string
# values into an integer.