# Write a program that prompts the user for their name. When they respond,
# write their name to a file called guest.txt

# Prompt name

print("Please enter your name: ")
name = input()

with open('names.txt', 'a') as file_object:
    file_object.write(f"{name}\n")