# Write a function called describe_city() that accepts the name of a city
# and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.

# Call your function for three different cities, at least one of which is not
# in the default country.

def describe_city(city_name, country="united kingdom"):
    """Prints a simple message of the city relating to the country."""
    print(f"{city_name.title()} is in {country.title()}")

describe_city("london")
describe_city("bangkok", "thailand")
describe_city("los angeles", "united states")