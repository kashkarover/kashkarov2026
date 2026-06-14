from random import *

def generate_password(length):
    password = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for _ in range(length):
        password += choice(chars)
    
    return password