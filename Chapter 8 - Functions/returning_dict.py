# Returning a Dictionary.
# A function can return any kind of value you need it to. Including data
# structures like lists and dictionaries.

# Example, the following function takes in parts of a name and returns a
# dictionary representing a person.

from distutils.command.build import build
import multiprocessing


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} # makes a dictionary
    return person

musician = build_person('jimmy', 'hendrix')
print(musician)

# We can extend to add an age as an optional parameter.
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} # makes a dictionary
    if age:
        person['age'] = age
    return person

musician = build_person('jimmy', 'hendrix', age=23)
print(musician)
musician = build_person('jimmy', 'hendrix')
print(musician)
