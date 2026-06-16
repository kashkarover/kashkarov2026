from fractions import Fraction as F
from math import gcd

n = int(input())
res = []
    
for i in range(1, n + 1):
    for j in range(n, 1, -1):
        if gcd(i, j) == 1 and j > i:
            res.append(F(i, j))
    
for num in sorted(res):
    print(num)