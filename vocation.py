vocation_polls = {}
active = True
# while loop to keep the program running as long as the user wants
while active:
	name = input("Please what is your name: ")
	vocations = input("please what skills would you like to learn: ")

	vocation_polls[name] = vocations
	# checking if the user wants to quit
	message = input("please would you like to take your poll next(yes or no): ")
# if statement to check if the user typed the right message 
	if message == 'no':
		active = False
	elif message != 'yes':
		print("try again")
		message = input("please would you like to take your poll next(yes or no): ")

		
print(f"\n---polls results---")
for name,vocation in vocation_polls.items():
	print(f"{name} would like to learn {vocation}")