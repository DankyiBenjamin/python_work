programming_words = {
	"if statement":"it is used to check for conditions in a program",
	"for loop": "it is used to loop through lsit and dictionaries",
	"variables":"used to store values "
}

print(" The meaning of the if statement is :" + programming_words["if statement"] + ".")
print(" \nThe meaning of the for loop :" + programming_words["for loop"] + ".")
print(" \nThe meaning of variables is :" + programming_words["variables"] + ".")

for key,values in programming_words.items():
	print(" \nThe meaning of the "+ key +" is :"+values+ ".")