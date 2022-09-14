'''.Write a Python program that reads two integersrepresenting a monthand day and
 prints the season for that month and day.
ExpectedOutput:Input the month (e.g. [1-12]): 07
Input the day: 31
Output: July, 31. Season is autumn'''

m = int(input("Input the month (e.g. [1-12]): "))
d= int(input("Input the day: "))

if m in (1, 3, 5, 7, 8, 10, 12):
    m_l = 31
elif m==2:
     m_l = 28
else: 
    m_l = 30
    if(d>30):
        print("ERROR")

if m==1:
    print("January", d, "Season is winter" )
elif m==2:
    print("February", d, "Season is winter" )
elif m==3:
    if d>19:
        print("March", d, "Season is spring")
    else:
        print("March", d, "Season is winter")
elif m==4:
    print("April", d , "Season is spring" )
elif m==5:
    print("May", d, "Season is spring" )
elif m==6:
    if d>20:
        print("June", d, "Season is summer")
    else:
        print("June", d, "Season is spring")
elif m==7:
    print("July", d,"Season is summer" )
elif m==8:
    print("August",d, "Season is summer")
elif m==9:
    if d>21:
        print("September",d, "Season is autumn")
    else:
        print("September",d, "Season is summer")
elif m==10:
    print("October",d,"Season is autumn")
elif m==11:
    print("November",d,"Season is autumn")
elif m==12:
    if d> 20:
        print("December",d,"Season is winter")
    else:
        print("December",d,"Season is autumn")
else:
    print("ERROR")



