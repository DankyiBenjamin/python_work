person_details = {
	'first_name': 'Ben-Oni',
	'last_name' : 'Dankyi',
	'age' : 19,
	'city' : 'Amasaman'
	}
print(person_details)

favourite_number = {
	'john':15,
	'stephen':17,
	'ben' : 19
}
print("John has " + str(favourite_number['john']) + " as his favorite number")
print("Stephen has " + str(favourite_number['stephen']) + " as his favorite number")
print("Ben has " + str(favourite_number['ben']) + " as his favorite number")
# to iterate over a dictionary use the item methon attached to the dictionary name and set two 
# variables since it will always return the key and the value 
for key, value in favourite_number.items():
	print("\nkey:" + key)
	print("value:" + str(value))

favourite_language = {
	'ben':'python',
	'dan':'java',
	'silvia':'c++'
}

for name,language in favourite_language.items():
	print(f"\n{name} likes {language}")

#  use the keys method to loop through only the keys in the dictionary
for name in favourite_number.keys():
	print(name.upper())