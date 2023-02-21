"""
Given a number n, write a python program to make and print the list of Fibonacci series up to n.
Input : n=7
Hint : first 7 numbers in the series
Expected output :
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

"""
n = 8

n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1