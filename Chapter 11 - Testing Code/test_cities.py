from difflib import unified_diff
import unittest
from city_functions import city_country as cc

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Test for 'Santiago, Chile' for its format."""
        formatted_name = cc('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Test for 'Santiago, Chile - population 500000' format."""
        formatted_name = cc('santiago', 'chile', 500000)
        self.assertEqual(formatted_name, 
        'Santiago, Chile - population 500000')
    
if __name__ == '__main__':
    unittest.main()