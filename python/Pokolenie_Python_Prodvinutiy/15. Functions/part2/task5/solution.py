def print_products(*args):
    products = [n for n in args if type(n) == str and len(n) != 0]
    
    if len(products) == 0:
        print('Нет продуктов')
    else:
        for i in range(1, len(products) + 1):
            print(f'{i}) {products[i -  1]}')