"""

Write a Python program to count the occurrences of each word in a given sentence.

"""

string = int(input("Enter a sentence : "))

my_list = string.split()
my_set = set(my_list)
my_dict = {}
for word in my_set:
    my_dict[word] = string.count(word)
print(my_dict)