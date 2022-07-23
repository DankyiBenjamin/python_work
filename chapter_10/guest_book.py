file_name = 'guest_book'
active = True

while active:
	quit = input("Please do you want to quit(Yes or no): ")
	if quit == "no":
		name = input("Please type your name: ")
		message = "Welcome " + name
		with open(file_name,'w') as file_object:
			file_object.write(message)
		with open(file_name,'r+') as file_object:
			guest = file_object.read()
			print(guest)
	else:
		active = False
