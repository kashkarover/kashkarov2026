from fractions import Fraction as F
from math import gcd

n = int(input())
res = []

if n % 2 != 0:
    a = [i for i in range(1, n // 2 + 1)]
    b = [i for i in range(n - 1, n // 2, -1)]
else:
    a = [i for i in range(1, n // 2)]
    b = [i for i in range(n - 1, n // 2, -1)]
    
for i in range(len(a)):
    if gcd(a[i], b[i]) == 1:
        res.append(F(a[i], b[i]))
    
print(max(res))