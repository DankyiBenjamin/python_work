import json
# always bring the file name before you read it 
file_name = 'number.json'

with open(file_name) as f_obj:
	# when reading a json file use the "f_obj" not the file name
	# the load funtion is used to load a json file to memory
	favorite_number = json.load(f_obj)
	print("I know your favorite number It is " + favorite_number)