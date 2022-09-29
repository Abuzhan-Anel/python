with open('cll.txt', 'r') as the_cll:
    all = the_cll.read().split('\n')
    for student in all:
        each = student.split()
        a = each[0].capitalize()
        b = each[1].capitalize()
        c = each[3]
        print(a,b,each[2],'301-',c)