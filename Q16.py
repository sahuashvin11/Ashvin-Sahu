"""
Counting the frequencies in a list using a dictionary in Python.
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

"""
list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

def CountFrequency(my_list):

	freq = {}
	for item in my_list:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	for key, value in freq.items():
		print ("% d : % d"%(key, value))

if __name__ == "__main__":
	CountFrequency(list)
