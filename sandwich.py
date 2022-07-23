foods = ['Banku','fufu','kenkey','rice','Banku','Banku']
served_foods = []


# while foods:
# 	prepare = foods.pop()
# 	print(f"\nI made your {prepare}")

# 	served_foods.append(prepare)
# print(served_foods)
# for food in served_foods:
# 	print(f"\nI prepared {food}")

while 'Banku' in foods:
	foods.remove('Banku')

print('There is no Banku')
print(foods)
