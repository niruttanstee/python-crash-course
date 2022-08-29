# Write a program that asks the user how many people are in their dinner
# group. If the answer is more than eight, print a message saying they'll
# have to wait for a table. Otherwise report that the table is ready.

num_people = input("How many people are in your group?: ")
num_people = int(num_people)

if num_people > 8:
    print("Please wait for a table to ready.")
else:
    print(f"Your table for {num_people} is ready.")