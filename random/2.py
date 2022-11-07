import random

tickets=[]
for i in range(100):
    a=random.randrange(1000000000, 9999999999)
    tickets.append(a)
c= random.sample(tickets, 5)
print(tickets)
print(c)