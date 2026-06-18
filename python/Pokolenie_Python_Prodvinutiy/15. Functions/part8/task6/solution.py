nums = filter(lambda x: x % 2 == 0 or x % 2 == 1 and x <= 47, numbers)
res = map(lambda x: x // 2 if x % 2 == 0 else x, nums)
print(*res)