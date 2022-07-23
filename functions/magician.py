magician_names = ['Haudini','Howard','Bronze']
magician_names_2 = magician_names[:]

def show_magicians(make_great2):
	# this function print the list of magicians
	for magician in magician_names_2:
		print(f"- {magician}")

def make_great(magician_names_2):
	# a fucntion to modify the list above
	# to modify a list use its index not the value of the list
	magician_names_2[0] = 'The great Haudini'
	magician_names_2[1] = 'The great Howard'
	magician_names_2[2] = 'The great Bronze'
	return make_great

make_great(magician_names_2)
show_magicians(make_great)

print(magician_names)

# print(magician_names)