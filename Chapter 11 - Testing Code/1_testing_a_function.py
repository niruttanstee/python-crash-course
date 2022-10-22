# Testing a function
# To learn about testing we need code to test. Here's a simple function that
# takes in a first and last name, and returns a neatly formatted full name.

# First we import the function and test it to see if it works.

from name_function import get_formatted_name as fn

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = fn(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

# We know that this code works. But what if we want the function to also handle
# middle names. As we do, we want to make sure we don't break the way the
# function handles names that have only a first and last name.
#
# Python provides an efficient way to automate the testing of a function's
# output. If we automate the testing of get_formatted_name() we can always be
# confident that the function will work when given the kinds of names we've
# written tests for.
#
# Unit Test and Test Cases
# The module unittest from the Python standard library provides tools for
# testing your code. 
#
# A unit test verifies that one specific aspect of a
# function's behavior is correct.
#
# A test case is a collection of unit tests that together prove that a function
# behaves as it's supposed to, within the full range of situations we can
# expect it to handle.
#
# A good test case considers all possible kinds of input a function could
# receive and includes tests to represent these.
#
# Test case with full coverage means a full range of unit tests covering all
# possible ways you can use a function.
