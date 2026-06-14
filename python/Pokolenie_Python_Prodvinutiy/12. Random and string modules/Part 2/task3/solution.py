from random import shuffle

def get_anagram(word):
    list_word = [ch for ch in word]
    shuffle(list_word)
    
    return ''.join(list_word)