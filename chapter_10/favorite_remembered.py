import json

file_name = 'number.json'

try:
	with open(file_name) as f_obj:
		# when reading a json file use the "f_obj" not the file name
		# the load funtion is used to load a json file to memory
		favorite_number = json.load(f_obj)
		print("I know your favorite number It is " + favorite_number)
except FileNotFoundError:
	file_name = 'number.json'
	favorite_number = input("please what is your favorite number: ")

	with open(file_name,'w') as f_obj:
		# the dump function is used to write to a json file 
		json.dump(favorite_number,f_obj)

	with open(file_name) as f_obj:
		favorite_number = json.load(f_obj)
else:
	print("Welcome" + favorite_number)