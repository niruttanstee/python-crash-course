# Make a dictionary containing three major rivers and the country each river
# runs through. Key = river, value = country.

# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

from itertools import count


rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"
}
for river, country in rivers.items(): # Remember the use of items()
    print(f"The {river} runs through {country}.")