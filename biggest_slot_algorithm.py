#Returns the longest streak of the second parameter in the list entered in the first parameter

def biggest_slot(list, looking_for):
	big_slot = 0
	var1 = 0
	for index in list:
		if index == looking_for:
			var1 += 1
			if var1 > big_slot:
				big_slot = var1
		else:
			var1 = 0
	return big_slot

def help():
	print("Returns the longest streak of the second parameter in the list entered in the first parameter")
	print("When there are 2 streaks that are equaly long it just returns the lenght of both of them")
	print("It doesnt return the index of the streak")
	print("First parameter = list, Second parameter = what your looking for")