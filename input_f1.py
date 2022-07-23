active = True
while active:
	prompt = "please what topping do you want(type quit when you are done):"

	pizza_toppings = input(prompt)
	if pizza_toppings == "quit":
		active = False
	else:
		print(f"You added {pizza_toppings} to your pizza")

