class User():
	"""User details"""
	def __init__(self, first_name,last_name,user_name,age,location):
		
		self.first_name = first_name
		self.last_name = last_name
		self.user_name = user_name
		self.age = age
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print(f"Your full name is {self.first_name + self.last_name}")
		print(f"Your user name is {self.user_name}")
		print(f"You leave at {self.location}")

	def greet_user(self):
		print(f"welcome {self.user_name}")


	def increament_login_attempts(self):
		# this method counts  the number of logins 
		self.login_attempts +=1
		print(f"You have login {str(self.login_attempts )} times")

	def reset_login_attempts(self):
		# resets the login to the default
		self.login_attempts = 0
		print("Your login login_attempts has been reset")
		print(self.login_attempts)

class Privileges():
	def __init__(self):
		self.privileges = ["can add post","can delete post","can ban users"]

	def show_privilages(self):
		# A method that tells what the admin does 
		print("The Admin  :")
		for privilage in self.privileges:
			print(privilage)



class Admin(User):
	"""This class inherits from the parent class User"""
	def __init__(self, first_name,last_name,user_name,age,location):
		super().__init__( first_name,last_name,user_name,age,location)
		# using an instance as an attribute
		self.privileges = Privileges()

		
	


# lois = User('Lois','Kwakyewaa','LoisK',20,'Amasaman')
# lois.describe_user()
# lois.greet_user()
# lois.increament_login_attempts()
# lois.increament_login_attempts()
# lois.increament_login_attempts()
# lois.increament_login_attempts()
# lois.reset_login_attempts()
# lois.increament_login_attempts()




		