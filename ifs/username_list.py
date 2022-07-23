user_names = ["Eric","Dan","lois","Boaz","Admin"]

# this if statement check if the list is empty or not
if user_names:
	for user_name in user_names:
		# this is used to differentiate between the admin and the employees
		if user_name == "Admin":
			print(f"Hello {user_name},would you like to see a status report")
		else:
			print(f"Hello {user_name}, thanks for logging in today")
else:
	print("there is no one at work today")


current_user = ["lois","boaz","Ben","Lena"]
new_users = ["Eric","Dan","Lois","Boaz","Admin"]
# used to cross check over a certain list to see its existance
for new_user in new_users:
	# this if statement checks the current_user to see if it doesnt have any names that
	# are the same as the ones in new_user
	if new_user.lower() in current_user:
		print(f"{new_user} already exist you have to set a new one")
	else:
		print(f"{new_user} is available you can sign up now")