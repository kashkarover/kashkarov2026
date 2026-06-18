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

def square(x):
    return x ** 2

def func(x):
    return len(str(abs(x))) == 2 and x % 7 == 0

res = filter(func, numbers)

print(sum(map(square, res)))