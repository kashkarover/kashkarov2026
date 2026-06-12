def scrabble(letters, word):
    flag = False
    letters_dict = {}
    word_dict = {}

    for ch in letters.lower():
        letters_dict[ch] = letters_dict.setdefault(ch, 0) + 1
    print(letters_dict)

    for ch in word.lower():
        word_dict[ch] = word_dict.setdefault(ch, 0) + 1
    print(word_dict)

    for key, value in word_dict.items():
        if key in letters_dict and letters_dict[key] >= value:
            flag = True
        else:
            flag = False
            break

    return flag