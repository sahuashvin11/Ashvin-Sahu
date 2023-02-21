"""
Write a Python program to unzip a list of tuples into individual lists.

"""


list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
 
 
res = [[i for i, j in list],
       [j for i, j in list]]
 
print("Modified list is : " + str(res))