def city_country(city,country,population = ''):
	"""A function that returns a city and a country"""
	if population:
		formatted_name = city+','+ country + ' -population' + ' ' + str(population)
	else:
		formatted_name = city+','+ country
	return formatted_name.title()

print(city_country("accra", "ghana",5000))
