import re

for _ in range(int(input())):
    a = input()
    if not re.match(r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$', a):
        print('Invalid')
    else:
        if re.search(r'(\d)\1\1\1', re.sub(r'-', '', a)):
            print('Invalid')
        else:
            print('Valid')