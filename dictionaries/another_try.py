people_who_should = ['ben','lois','dan','helina','silvia']

favourite_language = {
	'ben':'python',
	'dan':'java',
	'silvia':'c++'
}


for people in people_who_should:
	if people in favourite_language:
		print(f"{people}, thanks for taking your poll")
	else:
		print(f"{people}, please take your poll")