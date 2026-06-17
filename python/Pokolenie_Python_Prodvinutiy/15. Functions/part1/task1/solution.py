def matrix(n=0, m=0, value=0):
    
    if n == 0:
        res = [[value for _ in range(n + 1)] for i in range(m + 1)]
    elif m != 0:
        res = [[value for _ in range(m)] for i in range(n)]
    else:
        res = [[value for _ in range(n)] for i in range(n)]
    
    return res