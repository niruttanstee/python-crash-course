# The modulo operator (%) divides one number by another number and returns
# the REMAINDER

print(4 % 3) # = 1
print(5 % 3) # = 2 (rounded imperfect)
print(6 % 3) # = 0
print(7 % 3) # = 1

# It doesn't tell you how many times one number fits into another, only what
# the remainder is. When the number is divisible by another number, the
# remainder is 0, so the modulo operator always returns 0. We can use this
# fact to determine if a number is even or odd.

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0: # even numbers are always divisible by two, if modulo = 0
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

