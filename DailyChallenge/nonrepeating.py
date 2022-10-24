

def nonrepeat(s):
    letter_count = {}
    for letter in s:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
        print(letter_count)
    return -1

print(nonrepeat('loveleetcode'))

