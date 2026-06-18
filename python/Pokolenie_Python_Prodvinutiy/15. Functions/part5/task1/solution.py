def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def round2(x):
    return "%.2f" % x

print(*map(float, (map(round2, numbers))), sep='\n')