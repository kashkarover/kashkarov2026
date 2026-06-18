def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
        
    return result

def filter(function, items):
    result = []
    for item in items:
        if function(item):        
            result.append(item)

    return result

def func(x):
    return len(str(x)) == 3 and x % 5 == 2

def cube(x):
    return x ** 3

res = map(cube, filter(func, numbers))
print(*res, sep='\n')