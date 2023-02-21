"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.

"""
list = [10, 20, 10, 30, 40, 40]

def unique(list):

	unique_list = []

	for x in list:
		if x not in unique_list:
			unique_list.append(x)
	for x in unique_list:
		print (x)
        
print("The unique values from list is : ")
unique(list)
