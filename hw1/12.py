'''Write a Python program to find the median of threevalues.
ExpectedOutput:
input first number: 15
Input second number: 26
Input third number: 29
the median is 26.0'''

import statistics 

a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

lst = []
lst.append(a)
lst.append(b)
lst.append(c)
print(lst)

print(statistics.median(lst))