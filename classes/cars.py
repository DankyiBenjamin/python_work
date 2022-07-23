class Car():
	""" A simple attempt to represent a car"""
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.millage = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' +self.make + ' ' + str(self.model)
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {str(self.millage)} milles on it")

	def update_odometer_reading(self,milles):
		"""setting the odometer reading to the given value using a method"""
		if milles >= self.millage:
			self.millage = milles
		else:
			print("you cannot roll back an odometer")

	def increament_odometer(self, milles):
		# increasing the existing milles
		if milles > 0:
			self.millage +=milles
		else:
			print("You cannot add a negative number")

	def fill_gas_tank(self):
		print("This car has a 6l tank")

class Battery():
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=70): 
		"""Initialize the battery's attributes."""
   		self.battery_size = battery_size

   	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")



class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()

	
	# def fill_gas_tank(self):
	# 	# Electric cars dont need gass
	# 	print("This is an electric car you only need to charge")


my_car = Car('Audi', 'A4', 2022)
print(my_car.get_descriptive_name())
my_car.update_odometer_reading(23)
my_car.update_odometer_reading(4)
my_car.read_odometer()



my_used_car = Car('Land Cruiser','L300',2021)
my_used_car.update_odometer_reading(260)
my_used_car.read_odometer()
my_used_car.increament_odometer(-56)
print(my_used_car.get_descriptive_name())
my_used_car.read_odometer()

my_tesla = ElectricCar('Tesla','Model s',2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()