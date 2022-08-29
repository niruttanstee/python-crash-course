# Creating a glossary dictionary
# Use programming keyword as keys and values as meaning.
glossary = {
    "tuple": "An immutable (unchangeable) list that can only be defined once.",
    "append": "Appends an object to the back of the list.",
    "get": "Get method retrieves a value from a supplied key if exists.",
    "boolean": "A conditional state either resulting in true of false.",
    "[:]": "A method inserted at end of list to select all, before or after a position"
}

# We can clean up the code by using a loop instead of printing individually.
for word in sorted(glossary.keys()):
    print(f"\n{word}:\n{glossary[word]}")
