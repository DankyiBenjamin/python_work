from cars import cars_info
from magician import show_magicians as smg
print(cars_info('BMW','i8', color ='White',wing_doors = True))
print(smg)

def print_n():
	a = 4
	b = 6
	c = a +b
	print(c)

def print_m():
	a = 4
	b = 6
	c = a +b
	return c

result = print_n()
# result_2 = 1 +result
result_1 =print_m()
result_3 = result_1 +1
# print(result_2) 
print(result_3)
	

