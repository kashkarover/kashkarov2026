from random import shuffle

def get_secret_friend(students):
    n = len(students)
    friends = [name for name in students]
    
    flag = True
    while flag:
        flag = False
        shuffle(friends)
        for i in range(n):
            if friends[i] == students[i]:
                flag = True
                
    return {students[i]: friends[i] for i in range(n)}