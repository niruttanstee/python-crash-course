# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it's printed.

# After calling the function, print both of your lists to make sure that
# messages were moved correctly.

short_messages = [
    'hello there is is awesome',
    'ra ra rasputin',
    'shame really how he carried on',
    'there lives such a man'
]
sent_messages = []

def show_messages(short_messages):
    """Prints the short messages from a list."""
    if short_messages:
        for message in short_messages:
            print(f"{message}")
    else:
        print("Empty")

def send_messages(short_messages, sent_messages):
    """Prints text message from each list and moves messages to new list."""
    while short_messages:
        message = short_messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(short_messages, sent_messages)

print("\nSent message:")
show_messages(sent_messages)

print("\nShort messages:")
show_messages(short_messages)