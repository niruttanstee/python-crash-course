# Write a while loop that asks people why they like programming.
# Each time someone enters a reason, add their reason to a file that stores
# all the responses.

filename = "why_programming.txt"
prompt = "Why do you like programming?"
prompt = prompt + "\nEnter 'q' or 'quit' to end program: "

while True:
    reason = input(prompt)
    if reason == "q" or reason == "quit":
        break
    with open(filename, 'a') as file_object:
        file_object.write(f"{reason}\n")
