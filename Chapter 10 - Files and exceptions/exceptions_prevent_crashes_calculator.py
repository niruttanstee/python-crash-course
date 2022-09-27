# 2. Using exceptions to prevent crashes
# Creating a simple calculator that does only division:

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else: # The else block (any code that executes correctly goes to else)
        print(answer)

# Trace back can be a vulnerable source for attackers to learn more about the
# program. So we must fix the error with exceptions. Once fixed, the code is
# resistant to innocent user mistakes and malicious attacks.
