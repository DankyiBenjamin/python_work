
message =''
while message != "quit":
	

	car = input("please what car do you want: ")
	print(f"please let me see if i can find you a {car}")

	number_of_people = input("please how many people are in your dinning group: ")
	number_of_people = int(number_of_people)

	if number_of_people >= 8:
		print("please you would have to wait for a while")

	else:
		print("Your table is ready")

	number = int(input("please type a number: "))

	if number % 10 == 0:
		print("this number is a multiple of 10")
	else:
		print("this is not a multiple of 10")

	current_number = 0

	while current_number <= 5:
		print(current_number)
		current_number +=1

	message = input("message: ")

		

