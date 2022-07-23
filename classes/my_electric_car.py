from cars1 import Car,ElectricCar

my_car = Car("Range Rover","velar",2022)
print(my_car.get_descriptive_name())

my_tesla = ElectricCar('tesla','model s',2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()