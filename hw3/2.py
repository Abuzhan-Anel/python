f = open("myfile.txt", "x")
with open('aaa.txt') as the_aaa, open('bbb.txt') as the_bbb:
    for line1, line2 in zip(the_aaa, the_bbb):
        f.write(line1+line2)  
        print(line1+line2)
        
        

f = open("myfile.txt", "r")
print(f.read())