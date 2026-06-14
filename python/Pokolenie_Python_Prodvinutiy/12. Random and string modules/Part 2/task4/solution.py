from random import *

def generate_bingo():
    result = []
    nums_possible = [i for i in range(1, 76)]
    nums_in_game = sample(nums_possible, 24)
    
    for i in range(5):
        tmp = []
        for j in range(5):
            if i == 2 and j == 2:
                tmp.append(0)
            else:
                tmp.append(nums_in_game.pop())
                
        result.append(tmp)
    
    return result