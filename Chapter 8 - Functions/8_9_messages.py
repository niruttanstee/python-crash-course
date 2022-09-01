# Make a list containing a series of short text messages. Pass the list to
# a function called show_messages(), which prints each text messages.

short_messages = [
    'hello there is is awesome',
    'ra ra rasputin',
    'shame really how he carried on',
    'there lives such a man'
]

def show_messages(short_messages):
    """Prints the short messages from a list."""
    for message in short_messages:
        print(f"{message}")

show_messages(short_messages)