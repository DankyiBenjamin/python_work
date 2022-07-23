def cars_info(manufacturer,model_name,**other):
	cars = {}
	cars['Manufacturer'] = manufacturer
	cars['Model_name'] = model_name
	for key,value in other.items():
		cars[key] = value
	return cars


