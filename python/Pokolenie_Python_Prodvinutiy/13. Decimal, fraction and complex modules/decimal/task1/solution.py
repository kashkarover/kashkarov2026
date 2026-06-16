from decimal import Decimal as D

nums = [D(i) for i in s.split()]

print(max(nums) + min(nums))