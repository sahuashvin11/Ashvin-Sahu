"""
Write a Python program to get unique values from a list.

"""

list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")


def unique(list1):

	unique_list = []

	for x in list1:
		if x not in unique_list:
			unique_list.append(x)
	for x in unique_list:
		print(x)
unique(list1)

