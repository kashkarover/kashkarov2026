from fractions import Fraction as F

a, b = input(), input()
m, n = F(a), F(b)
print(f'{a} + {b} = {m + n}')
print(f'{a} - {b} = {m - n}')
print(f'{a} * {b} = {m * n}')
print(f'{a} / {b} = {m / n}')