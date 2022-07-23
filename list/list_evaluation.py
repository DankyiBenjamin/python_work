
# use the split function to take a list of strings
requested_toppings = list(map(str, input().split(',')))
print(requested_toppings)

# this check if the list is empty or not
if requested_toppings:
	for topping in requested_toppings:
		print(f"You ordered for {topping} on your pizza")

else:
	print("Do you want a plain pizza")


