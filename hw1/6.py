'''Write a Python program to sum of two given integers.However, if thesum is between 15 to 20 it will return 20.'''

a = int(input())
b = int(input())
sum = a + b
if (15<= sum <= 20):
    print("20")
else:
    print(sum)