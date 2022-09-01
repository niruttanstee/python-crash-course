# Write a function called city_country() that takes in the name of a city and
# its country. The function should return a string formatted: 
# "Santiago, Chile"

# Call your function with at least three city-country pairs, and print the values
# that are returned.

def city_country(city_name, country):
    """Return a string of city and country."""
    formatted = f"{city_name}, {country}"
    return formatted.title()

print(city_country('london', 'united kingdom'))
print(city_country('paris', 'france'))
print(city_country('bangkok', 'thailand'))