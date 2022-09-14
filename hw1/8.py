print("Input lengths of the triangle sides:")
a = input("x = ")
b = input("y = ")
c = input("z = ")
if(a==b==c):
    print("An equilateral triangle")
elif(a==b or b==c or a==c):
    print("An isosceles triangle")
else:
    print("A scalene triangle")