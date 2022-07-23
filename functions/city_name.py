def city_country(city,country):
	print(f"{city},{country}")
	return ''

print(city_country("Accra","Ghana"))
print(city_country("Kumasi","Ghana"))
print(city_country("LA","USA"))

def album():
	active = True
	
	while active:
		name = input("please type the name of the artist or quit to stop: ")
		title = input("Please type title of the album: ")
		number_of_songs = input("please type the number of songs in the album")
		album_dict = {"album_name":name,"album_title":title,'number':number_of_songs}
		print(album_dict)
		repeat = input("please would you like to continue: ")


		if repeat == "no":
			active = False
	
		
		
			

album()
