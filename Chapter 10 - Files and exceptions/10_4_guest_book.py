# Write a while loop that prompts users for their name.

prompt = "Please enter your name without capitalization: "
name = input(prompt)

# When they enter their name, print a greeting to the screen and add a line
# recording their visit in a file called guest_book.txt, Make sure each entry
# appears on a new line in the file.

print(f"Welcome, {name.title()}.")

with open('guestbook.txt', 'a') as file_object:
    file_object.write(f"{name} has visited.\n")