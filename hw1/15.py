'''Write a Python program to create the multiplicationtable (from 1 to10) of a number.
ExpectedOutput:
Input a number: 6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 306 x 6 = 366 x 7 = 426 x 8 = 486 x 9 = 546 x 10 = 60'''

num = int(input("Input a number: "))

def my_function(number):
    for x in number:
        print( num , "x", x , "=",  x*num)

txt = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_function(txt)

