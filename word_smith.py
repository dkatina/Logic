import re

words = ['this' , 'is', 'a', 'sentence', '.']
def reverse_word(word):
    word_list = []
    for letter in word:
        word_list.append(letter)
    l = 0
    r = len(word_list) - 1
    while l <= r:
        word_list[l], word_list[r] = word_list[r], word_list[l]
        l +=1
        r -= 1
    return ''.join(word_list)
    

def reverser(alist):
    l = 0
    r = len(alist) - 1
    while l <= r:
        alist[l] = reverse_word(alist[l])
        alist[r] = reverse_word(alist[r])
        alist[l], alist[r] = alist[r], alist[l]
        l += 1
        r -= 1
    return alist



reverser(words)
print(words)

word = '!7word!'

clean_word = re.sub(r'\W', '', word)
print(clean_word)