from random import *
import string

n, m = int(input()), int(input())
chars_lower = [ch for ch in string.ascii_lowercase if ch not in 'lI1oO0']
chars_upper = [ch for ch in string.ascii_uppercase if ch not in 'lI1oO0']
chars_digits = [ch for ch in string.digits if ch not in 'lI1oO0']
chars = [ch for ch in (string.ascii_letters + string.digits) if ch not in 'lI1oO0']

def generate_password(length):
    password = sample(chars, length - 3)
    password.append(choice(chars_lower))
    password.append(choice(chars_upper))
    password.append(choice(chars_digits))
    shuffle(password)
    
    return ''.join(password)

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(m))

generate_passwords(n, m)