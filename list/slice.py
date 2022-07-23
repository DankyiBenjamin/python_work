letters = ["p","r","o","g","r","a","m"]
letter1 = letters[:3]
letter2 =  letters[3:6]
print(f"the middle three items of the initial list is {letter2}")
print(f"the first three items of the initial list is {letter1}")
for letter in letters[:3]:
	print(letter.upper())

list_of_pizza = ["Banku", "fufu", "kokonte"]
friends_list = list_of_pizza[:]
list_of_pizza.append("fish")
friends_list.append("meat")
print(list_of_pizza)
print(friends_list)
for pizza in list_of_pizza:
	print(f"My favorite pizza is {pizza}")
	break

for pizzas in friends_list:
	print(f"My favorite pizza is {pizzas[2]}")
	break
