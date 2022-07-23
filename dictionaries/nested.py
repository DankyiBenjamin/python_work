person_details = {
	'bDankyi' :{
	'first_name': 'Ben-Oni',
	'last_name' : 'Dankyi',
	'age' : 19,
	'city' : 'Amasaman'},

	'lovely' :{
	'first_name': 'Boaz',
	'last_name' : 'Afful',
	'age' : 20,
	'city' : 'Dawhenya'

	}

	}
	# reassigning a value in a nested dictionary
person_details['lovely']['first_name'] = 'Boa'
for user_name, user_info in person_details.items():
	print(f"\nUser name: {user_name}")
	full_name = user_info['first_name'] + " " + user_info["last_name"]

	print(f"full_name : {full_name}")
	print(f"Location : {user_info['city']}")