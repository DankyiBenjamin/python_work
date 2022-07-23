guest = ["ofosu addo","juliana","harry nartey"]

for names in guest:
	print(f"{names}, you are invited to my dinner")

cannot_make = guest.pop(0)
print(f"{cannot_make}, cannot attend the dinner")
guest.insert(0,"Ben")
print("the new list of invites are: ")
print(guest)
for names in guest:
	print(f"{names}, you are invited to my dinner")

print("Hurry, I just found a bigger tables which means more people, more food")
guest.insert(2, "Lois")
guest.insert(0, "Abigail")
guest.append( "Lena")
print("this is the new list")
print(guest)

for names in guest:
	print(f"{names}, you are invited to my dinner")

number_of_people = len(guest)
print(f"I am inviting {number_of_people} people to the dinner")