from random import choice
# Make a list or tuple containing a series of 10 numbers and five letters.

lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

# Randomly select four numbers or letters from the list and print a message
# saying that any ticket matching these four numbers or letters wins a prize.

lottery_result = ''

count = 0
while count < 4:
    selected_number = choice(lottery_numbers)
    
    if isinstance(selected_number, int):
        if selected_number < 10:
            lottery_result += f" 0{selected_number} "
        else:
            lottery_result += f" {selected_number} "
    else:
        lottery_result += f" {selected_number}"
    # Don't forget this
    count += 1

# Strip any leading or trailing whitespaces
lottery_result = lottery_result.strip()

print("--- Any ticket matching these four numbers or letters wins a prize ---")
print(f"{lottery_result}")
