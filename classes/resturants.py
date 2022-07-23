class Restaurant():
	"""describe a restaurant with the food they sell
	or if they are opened or not"""
	def __init__(self,restaurant_name,cusine_type):
		""" intialize retaurant name and cusine types"""
		self.restaurant_name = restaurant_name
		self.cusine_type = cusine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The name of this Restaurant is {self.restaurant_name}")
		print(f"We serve {self.cusine_type}")

	def open_resturant(self):
		print(f"We are open")

	def read_number_served(self, served):
		# takes the number of served customers
		if served > 0:
			self.number_served = served
			print(f"We have served {self.number_served} customers")
		else:
			print("Cannot serve a negative number of people")
			print(f"We have served {self.number_served} customers")


class IceCreamStand(Restaurant):
	"""This class inherits from the restaurant class"""
	def __init__(self,restaurant_name,cusine_type,flavors):
		super().__init__(restaurant_name,cusine_type)
		self.flavors = flavors
	def display_flavors(self):
		print("You chose " + self.flavors + " .")





my_restaurant = Restaurant("Dankyi's","Local dishes")
lena_restaurant = Restaurant("Lena's","Forieng_dishes")
abi_restaurant = Restaurant("Rhiner","French_dishes")
restaurnt = Restaurant("Dankyi's","Local dishes")
my_flavor = IceCreamStand("Dankyi's",'Ice cream','straw')

		
my_restaurant.describe_restaurant()
my_restaurant.open_resturant()
lena_restaurant.describe_restaurant()
lena_restaurant.open_resturant()
abi_restaurant.describe_restaurant()
abi_restaurant.open_resturant()
restaurnt.read_number_served(-9)
my_flavor.display_flavors()