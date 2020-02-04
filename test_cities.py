import unittest
from city_functions import city_func

class TestCityCountry(unittest.TestCase):
    """Test for function city_func"""

    def test_city_country_display(self):
        city_country = city_func('berlin', 'germany')
        self.assertEqual(city_country, 'Berlin is in Germany.')

    def test_city_country_when_display(self):
        city_country2 = city_func('berlin', 'germany', 'summer')
        self.assertEqual(city_country2, 'Berlin is in Germany. I will visit it in Summer.')


if __name__ == '__main__':
    unittest.main()