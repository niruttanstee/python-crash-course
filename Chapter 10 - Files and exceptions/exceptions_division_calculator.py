# Python uses special objects called EXCEPTIONS to manage errors that arises
# during a program's execution. Whenever an error occurs that makes Python
# unsure what to do next, it creates an exception object. We can write code
# to handle the exception so the program will continue running. The program
# however, will halt if we do not handle the exception and it will show a
# TRACEBACK.

# Exceptions are handled with TRY-EXCEPT blocks.

# 1. Handling a ZeroDivisionError Exception
# It's impossible to divide a number by zero so it'll create an exception.
# print(5/0) # an error will occur (ZeroDivisionError: division by zero)

# To counter this we can use a try-except block:
try:
    print(5/0) # an error will occur
except ZeroDivisionError: # add the exception object here to do something
    print("You can't divide by zero!") # do something if exception occurs

# Python skips over the except block if there are no errors in the try block.