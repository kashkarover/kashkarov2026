from fractions import Fraction as F

n = int(input())
nums = [i for i in range(1, n + 1)]
res = 0

for num in nums:
    res += F(1, num ** 2)
    
print(res)