# You can analyze text files containing entire books. Many classic works of
# literature are available as simple text files because they are in public
# domain.

# We'll use book.txt containing Alice in Wonderland and try to count the
# number of words in the text. We'll use a string method split(), which can
# build a list of words from a string.

# Example of what split() does:

title = "Alice in Wonderland"
print(title.split()) # ['Alice', 'in', 'Wonderland']

# Now we'll count the number of words in the entire book text file:

filename = 'book.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words) # len() gets the number of items in the list
    print(f"The file {filename} has about {num_words} words.")
