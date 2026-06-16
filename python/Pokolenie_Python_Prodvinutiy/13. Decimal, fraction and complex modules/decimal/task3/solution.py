from decimal import *

d = input().lstrip('-')
num = Decimal(d).as_tuple().digits

if len(d) - 1 - len(num) == 1:
    print(max(num))
else:
    print(max(num) + min(num)) 