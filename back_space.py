# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols.
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""








def back_space(string):
    backspace = 0
    word =[]
    for char in string[::-1]:
        if char == '#':
            backspace += 1
        elif backspace == 0:
            word.insert(0, char)
        else:
            backspace -= 1

    return "".join(word)

print(back_space('abc#d##c'))
