nums = [num for num in input().split()]

def comparator(num):
    sums = 0
    for n in num:
        sums += int(n)
    return sums

print(*sorted(nums, key=comparator))