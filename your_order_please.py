



def order(sentence):
    sentence = sentence.split(' ')
    new_sent = list(range(len(sentence)))
    print(sentence)
    for word in sentence:
        if '1' in word: 
            new_sent[0] = word
        elif '2' in word: 
            new_sent[1] = word
        elif '3' in word: 
            new_sent[2] = word
        elif '4' in word: 
            new_sent[3] = word
        elif '5' in word: 
            new_sent[4] = word
        elif '6' in word: 
            new_sent[5] = word
        elif '7' in word: 
            new_sent[6] = word
        elif '8' in word: 
            new_sent[7] = word
        elif '9' in word: 
            new_sent[8] = word
    return " ".join(new_sent)

order('')