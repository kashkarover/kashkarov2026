from random import *

def generate_ip_address():
    nums = [str(randint(1, 255)) for _ in range(4)]
    shuffle(nums)
    
    return '.'.join(nums)