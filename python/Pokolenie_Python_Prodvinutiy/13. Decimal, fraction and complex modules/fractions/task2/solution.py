from fractions import Fraction as F

nums = [F(i) for i in s.split()]

print(max(nums) + min(nums))