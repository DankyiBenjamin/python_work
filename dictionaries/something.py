pizza_crust = []
pizza_toppings = []


crust = input(" please what crust do you want")
print("please what toppings do you want separate them with a comma")
toppings = input().split(",")

pizza_crust.append(crust)
pizza_toppings.append(toppings)

for crust in pizza_crust:
	print(f"you like {crust} crust")

for toppings in pizza_toppings:
	print(f'you like {toppings} on your pizza')

