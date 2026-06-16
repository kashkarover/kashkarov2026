from decimal import Decimal as D

nums = [D(i) for i in s.split()]

print(sum(nums))
print(*sorted(nums, reverse=True)[:5])