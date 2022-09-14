'''.Write a Python program to calculate the sum andaverage of ninteger numbers (input from the user).
 Input 0 to finish.'''

cnt = 0
sum = 0
num = 1

while num != 0:
    num= int(input())
    sum = sum + num
    cnt+= 1

if cnt == 0:
    print("Input numbers")
else:
    print("Average and Sum : ", sum / (cnt-1), sum)
