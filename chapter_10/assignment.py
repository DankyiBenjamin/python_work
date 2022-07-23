file_name = 'learning_python.txt'
file_name2 = 'numbers.txt'

with open(file_name) as file_object:
	messages = file_object.readlines()
	for message  in messages:
		print(message.replace("python", 'C').rstrip().title())

with open(file_name2, 'w') as file_object:
	messages = 12345
	messages = str(messages)
	for message in messages:
		print(file_object.write(message))

