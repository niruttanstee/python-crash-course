# Using CONTINUE in a loop.
# Rather than breaking out of a loop entirely without executing the rest of
# of its code, we can use the CONTINUE statement to return to the beginning
# of the loop based on the result of a conditional test.

# Scenario, a loop that counts from 1 to 10 but prints only the odd numbers in
# that range.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # if number is even start the loop again so it won't print the line below
    print(current_number)