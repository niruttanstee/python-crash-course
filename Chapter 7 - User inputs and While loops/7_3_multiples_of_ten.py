# Ask the user for a number, and then report whether the number is a multiple
# of 10 or not.

prompt = "Please enter a number, so I can tell you whether its a multiple of"
prompt += " 10 or not: "
number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")