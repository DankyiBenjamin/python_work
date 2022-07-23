def first_twelve(number):
	# a function that prints the first 12 multiples 
	# of a number
	for x in range(13):
		print(x*number)

def last_number(number,last_num):
	"""This funtion prints the multiples of a number till the last number 
	specified the user"""
	for x in range((last_num + 1)):
		print(x * number)


def first_last_number(number,first_num,last_num):
	"""This funtion prints the multiples of a number from user specification to
	 the last number specified the user"""
	for x in range(first_num,(last_num+1)):
		print(x*number)


message = input("Do you want to  get the fist 12?(Yes or NO): ").upper()
if message =="YES" or message == "Y":
	number = int(input("please what number do you want the multiples of: "))
	first_twelve(number)
else:
	message_2 = input("Do you want to specify the start and stop?(Yes or NO): ").upper()
	if message_2 == "YES" or message_2 == "Y":
		number = int(input("please what number do you want the multiples of: "))
		first_num = int(input("please where do you want to start from: "))
		last_num = int(input("please what is the last number: "))

		first_last_number(number,first_num,last_num)
	else:
		number = int(input("please what number do you want the multiples of: "))
		last_num = int(input("please what is the last number: "))
		last_number(number,last_num)




