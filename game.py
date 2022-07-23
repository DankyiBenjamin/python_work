# number of times you can try
ATTEMPTS = 3
NUMBER = 5

# check if he still have an attempt
while ATTEMPTS > 0:
	guess = int(input("guess a number: "))
	ATTEMPTS -=1
	if guess == NUMBER:
		print("you won")
		break
	else:
		print("Try again, you have " + str(ATTEMPTS) + " attemps left")



	