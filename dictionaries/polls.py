
people_who_should = ['ben','lois','dan','helina','silvia']

favourite_language = {
	'ben':'python',
	'dan':'java',
	'silvia':'c++'
}
key_list = []
# creating a list from the dictionary
for k in favourite_language.keys():
	key_list.append(k)
for people in people_who_should:
	if people in key_list:
		print(f"{people}, thanks for taking the poll")
	else:
		print(f"{people}, please take your poll")

# 9

