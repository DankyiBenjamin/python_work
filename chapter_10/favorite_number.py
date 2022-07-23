import json

file_name = 'number.json'
favorite_number = input("please what is your favorite number: ")

with open(file_name,'w') as f_obj:
	# the dump function is used to write to a json file 
	json.dump(favorite_number,f_obj)



