emojis = {
    'яблоко': '🍎', 'хлеб': '🍞', 'конфеты': '🍬', 'лимон': '🍋',
    'морковь': '🥕', 'огурец': '🥒', 'помидор': '🍅', 'яйцо': '🥚',
    'чеснок': '🧄', 'авокадо': '🥑', 'спички': '🥢', 'соль': '🧂',
    'филе говядины': '🥩', 'киви': '🥝', 'лук': '🧅', 'сыр': '🧀',
}

def print_product_list(product_list):
    products = list(set(product_list))

    for product in products:
        if product in emojis:
            print(f'{emojis[product]}: {product_list.count(product)}')
        else:
            print(f'{product}: {product_list.count(product)}')