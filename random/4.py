import random
import string

str = []
for i in range(5):
    a= random.choice(string.ascii_letters)
    str.append(a)
full = ''.join(str)
print(full)