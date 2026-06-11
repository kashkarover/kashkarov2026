def dict_diff(data1, data2):
    res = {}

    for key in data1.keys():
        if key not in data2:
            res[key] = 'deleted'
        else:
            if data1[key] == data2[key]:
                res[key] = 'unchanged'
            else:
                res[key] = 'changed'
                
    for key in data2.keys():
        if key not in data1:
            res[key] = 'added'

    return res