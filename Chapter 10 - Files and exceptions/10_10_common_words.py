# Counting the common words from large volume of text.
# We can use the method count() to count but it also helps if we use lower()
# to make all text lowercase to count all same words.

# Write a program that reads the book and determines how many times the word
# 'the' appears in each text. This will be an approximation because it will
# also count words such as 'then' and 'there'.

# The try counting the word with a space behind to see how lower the count is.

filepath = '/Users/nirutt/Documents/Code/python/crash_course/python-crash-course/Chapter 10 - Files and exceptions/The Roly-Poly book.txt'

try:
    with open(filepath) as f:
        content = f.read()
        similar_words = content.count('the')
        similar_words_improved = content.count('the ')
        print(f"'the' word has been found {similar_words}")
        print(f"'the ' word has been found {similar_words_improved}")
except FileNotFoundError:
    print(f"The book filepath does not exist: {filepath}")