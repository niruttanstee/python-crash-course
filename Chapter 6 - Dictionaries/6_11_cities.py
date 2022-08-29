# Make a dictionary called cities. Use the names of three cities as keys in
# your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one
# fact about that city. The keys for each city's dictionary should be 
# something like country, population and all information about the city.
# Print the name of each city  and all of the information you have stored
# about it.

# nested dictionary in a dictionary

cities = {
    'london': {
        'country': 'united kingdom',
        'fact': 'the largest city in the UK',
        'population': 9_000_000,
    },
    'paris': {
        'country': 'france',
        'population': 2_100_000,
        'fact': 'established in 300 BC',
    },
    'rio': {
        'country': 'brazil',
        'population': 6_700_000,
        'fact': 'second most populous city in Brazil',
    }
}

for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tInfo: {info['fact'][:1].title()}{info['fact'][1:]}.")
    