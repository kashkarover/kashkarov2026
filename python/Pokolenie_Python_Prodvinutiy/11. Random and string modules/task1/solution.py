from random import *

def coin_flip():
    res = randint(0, 1)
    return 'Решка' if res == 1 else 'Орел'