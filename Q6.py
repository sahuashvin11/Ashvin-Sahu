"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if
'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string


"""

string = input("Enter a String : ")

not_position = string.find('not')
poor_position = string.find('poor')

if not_position < poor_position and not_position != -1:
    new_string = string[:not_position] + 'good' + string[poor_position+4:]
else:
    new_string = string

print(new_string)