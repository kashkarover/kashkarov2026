spendings_dict = {}

def show_top_categories(spendings, num):
    for i in range(len(spendings)):
        spendings_dict[spendings[i][0]] = spendings_dict.get(spendings[i][0], 0) + spendings[i][1]
        
    sorted_spendings_dict = sorted(sorted(spendings_dict.items(), key=lambda value: value[1], reverse=True)[:num], key=lambda key: key[0])

    [print(item[0]) for item in sorted_spendings_dict]