from decimal import *

d = Decimal(input())

res = d.exp() + d.ln() + d.log10() + d.sqrt()

print(res)