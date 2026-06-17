def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def square_root(x):
    return x ** 0.5

def absolute(x):
    return abs(x)

def sin(x):
    from math import sin
    return sin(x)

ops = {'квадрат': square, 'куб': cube, 'корень': square_root, 'модуль': absolute, 'синус': sin}

x, op = int(input()), input()

print(ops[op](x))