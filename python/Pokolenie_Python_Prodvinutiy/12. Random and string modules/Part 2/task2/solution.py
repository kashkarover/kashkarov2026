from random import *
import string

def generate_index():
    result = ''
    
    for i in range(7):
        if i == 2 or i == 4:
            result += str(randint(0, 99))
        elif i == 3:
            result += '_'
        else:
            result += choice(string.ascii_uppercase)
            
    return result