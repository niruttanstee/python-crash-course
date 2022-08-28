# Using AND to check multiple conditions.
# To check whether two conditions are both True simultaneously.
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False as age_1 is not >= 21

# To improve readability we can...
result = (age_0 >= 21) and (age_1 >= 21) # Use parentheses

# Using OR to check multiple conditions.
# To check whether either the two conditions are true.
print(age_0 >= 21 or age_1 >= 21) # True as age_1 is >= 21
print(age_0 >= 25 or age_1 <= 17) # False as neither is true