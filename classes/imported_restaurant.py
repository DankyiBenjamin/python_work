import resturants


my_restaurant = resturants.Restaurant("Dankyi's","Local dishes")
lena_restaurant = resturants.Restaurant("Lena's","Forieng_dishes")
abi_restaurant = resturants.Restaurant("Rhiner","French_dishes")
restaurnt = resturants.Restaurant("Dankyi's","Local dishes")
my_flavor = resturants.IceCreamStand("Dankyi's",'Ice cream','straw')

		
my_restaurant.describe_restaurant()
my_restaurant.open_resturant()
lena_restaurant.describe_restaurant()
lena_restaurant.open_resturant()
abi_restaurant.describe_restaurant()
abi_restaurant.open_resturant()
restaurnt.read_number_served(-9)
my_flavor.display_flavors()