# Move every letter in the provided string forward 10 letters through the alphabet.
# If it goes past 'z', start again at 'a'.
# Input will be a string with length > 0.

def move_ten(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return ''.join(alphabet[alphabet.index(letter) - 16] if alphabet.index(letter) >= 16 else alphabet[alphabet.index(letter)+10] for letter in string.lower())

print(move_ten('testcase'))

    # new_string = ''
    # for letter in string:
    #     if alphabet.index(letter) >= 16:
    #         index = alphabet.index(letter) - 16
    #         new_string += alphabet[index]
    #     else:
    #         index = alphabet.index(letter) + 10
    #         new_string += alphabet[index]
    # return new_string



