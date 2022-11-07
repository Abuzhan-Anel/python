import random
import string

lts = ["A","b","r","d","l","K","L","s","E"]
f = []
full = ''.join(lts)
for i in range(5):
    x = random.choice(lts)
    f.append(x)
ful = ''.join(f)
print(ful)
print(full)