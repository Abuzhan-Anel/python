str = ""

for row in range(0,7):
    for col in range(0,7):
        if((col==1 and 0<= row <=6) or (col==2 and row==0 and row == 3) or (col==3 and row==0 and row==3 and row==4) or (col==4 and row==0 and row==3) or (col==5 and row==1 and row==2 and row==6)):
            str= str + "*"
        else:
            str = str + ""
    str = str + "\n"
print(str)