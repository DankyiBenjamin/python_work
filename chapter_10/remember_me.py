import json

def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
			
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	""" Prompt for a new user"""
	filename = 'username.json'
	username = input("please type in your name new user: ").upper()


	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username

def greet_user(verify):
	"""Greet the user by name"""
	username = get_stored_username()
	if username == verify:
		print(f"Welcome back {username}")
	else:
		username = get_new_username()
		print(f"Welcome {username} we will remember you when you come again")



verify = input("please what is your name: ").upper()

greet_user(verify)	
