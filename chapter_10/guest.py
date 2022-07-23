guest_name = input("please what is your name: ")
file_name = 'guest.txt'

with open(file_name,'w') as file_object:
	file_object.write(guest_name)

with open(file_name,'w') as file_object:
	name = file_object.read()
	print(name)


	