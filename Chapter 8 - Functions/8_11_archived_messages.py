# Call the function send-messages() with a copy of the list of messages. After
# calling the function, print both of your lists to show that the original
# list has retained its messages.

def send_messages(short_messages, sent_messages):
    """Prints text message from each list and moves messages to new list."""
    while short_messages:
        message = short_messages.pop()
        print(message)
        sent_messages.append(message)

short_messages = [
    'hello there is is awesome',
    'ra ra rasputin',
    'shame really how he carried on',
    'there lives such a man'
]
sent_messages = []

send_messages(short_messages[:], sent_messages)
print(short_messages)
print(sent_messages)