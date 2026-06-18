def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
        
    return result

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)

    return acc

def square(x):
    return x ** 2

def add(x, y):
    return x + y

res = map(square, numbers)

print(reduce(add, res, 0))