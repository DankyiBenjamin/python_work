responses = {}
polling_active = True
while polling_active:
	name = input("please type your name: ")
	response = input("what is your favorite food:")

	responses[name] = response

	repeat = input("please will you like to continue 'yes or no': ")

	if repeat == "no":
		polling_active = False

print("\n --Poll results--")
for name,response in responses.items():
	print(f"{name} likes {response}")