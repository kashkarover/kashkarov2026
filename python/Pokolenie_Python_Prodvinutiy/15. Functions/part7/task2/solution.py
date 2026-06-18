from functools import reduce

lst = list(filter(lambda pop: pop[1] >= 1e7 and pop[2] == 'primary', data))
sorted_lst = sorted(lst, key=lambda name: name[0])
cities = map(lambda name: name[0], sorted_lst)
res = 'Cities: ' + reduce(lambda a, b: a + ', ' + b, cities)
print(res)