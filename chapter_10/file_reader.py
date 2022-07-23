# the with is used to open and close a file automatically
# with open('pi_million_digits.txt') as file_object:
# 	for line in file_object:
# 		print(line.rstrip())

with open('pi_million_digits.txt') as file_object:
	# readline() is used to store files in a list form
	lines = file_object.readlines()
	
	pi_string = ''
	for line in lines:
		pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your bday appears in the first millon digits of pi!")
else:
	print("oops your bday is not in")