'''Write a Python program to get next day of a givendate.
ExpectedOutput:
Input a year: 2016
Input a month [1-12]: 08
Input a day [1-31]: 23
The next date is [yyyy-mm-dd] 2016-8-24'''

y = int(input("Input a year: "))
m = int(input("Input a month [1-12]:"))
d = int(input("Input a day [1-31]: "))

if y % 400 == 0:
    l_y = True
elif y % 100 ==0:
    l_y = False
elif y % 4 == 0:
    l_y = True
else:
    l_t = False


if m in (1, 3, 5, 7, 8, 10, 12):
    m_l = 31
elif m==2:
    if l_y is True:
        m_l = 29
    else:
        m_l = 28
else: 
    m_l = 30

if d<m_l: 
    d +=1 
else:
    d=1 
    if m == 12:
        m = 1
        y +=1
    else:
        m+=1

print("The next date is [yyyy-mm-dd] ", y,"-",m,"-",d)

