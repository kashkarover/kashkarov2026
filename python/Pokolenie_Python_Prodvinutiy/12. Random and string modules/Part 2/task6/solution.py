from random import sample
import string

n, m = int(input()), int(input())
chars = [ch for ch in (string.ascii_letters + string.digits) if ch not in 'lI1oO0']

def generate_password(length):
    return ''.join(sample(chars, length))

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(m))

generate_passwords(n, m)