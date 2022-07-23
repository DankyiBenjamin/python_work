import unittest
from city_function import city_country

class CityTestCase(unittest.TestCase):
	"""Test for city_funtion.py"""

	def test_city_country_format(self):
		"""Will it be of format Accra,Ghana?"""
		formatted_city = city_country('accra','ghana')
		self.assertEqual(formatted_city,'Accra,Ghana')

	def test_city_country_populatin_format(self):
		""" Will it be of the format Accra.Ghana -Population xxx"""
		formatted_city_population = city_country('accra','ghana', 5000)
		self.assertEqual(formatted_city_population,'Accra,Ghana -Population 5000')
unittest.main()