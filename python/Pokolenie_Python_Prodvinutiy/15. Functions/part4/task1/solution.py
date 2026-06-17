def comparator(number):
    return sum(number) / len(number)

print(min(numbers, key=comparator))
print(max(numbers, key=comparator))