from random import randint

def generate_lottery_ticket():
    result = []
    
    while len(result) < 7:
        x = randint(1, 49)
        if x not in result:
            result.append(x)
            
    return ' '.join(map(str, sorted(result)))