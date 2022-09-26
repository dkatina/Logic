

from audioop import add


def hold_words():
    x = ''
    def add_word(word=None):
        nonlocal x
        if word is None:
            return print(x)
        x += ' ' + word
    return add_word

words = hold_words()
words("Hello")
words("World!")
words("How")
words("are")
words("you?")
words()

