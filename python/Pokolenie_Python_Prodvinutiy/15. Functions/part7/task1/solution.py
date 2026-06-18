from functools import reduce

map_result = list(map(lambda num: round(num ** 2, 1), floats))
filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)