# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

#https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

from gettext import find


def valid_braces(string):
    for letter in string:
        if letter == '(':
            if ')' in string:
                i = string.index(letter)
                if not find_paran(string[i:]):
                    return False
                else:
                    string = string.replace('(', '1', 1)
                    string = string.replace(')', '1', 1)
                    print(string)
            else:
                return False

        elif letter == '{':
            if '}' in string:
                i = string.index(letter)
                if not find_curly(string[i:]):
                    return False
                else:
                    string = string.replace('{', '1', 1)
                    string = string.replace('}', '1', 1)
                    print(string)
            else:
                return False

        elif letter == '[':
            if ']' in string:
                i = string.index(letter)
                if not find_brace(string[i:]):
                    return False
                else:
                    string = string.replace('[', '1', 1)
                    string = string.replace(']', '1', 1)
                    print(string)
            else:
                return False

    if ')' and '}' and ']' not in string:
        return True
    return False

def find_paran(string):
    open_paran =  string.index('(')
    close_paran = string.index(')')
    if open_paran > close_paran:
        return False
    if (close_paran - open_paran) % 2 == 1:
        return True

def find_curly(string):
    open_paran =  string.index('{')
    close_paran = string.index('}')
    if open_paran > close_paran:
        return False
    if (close_paran - open_paran) % 2 == 1:
        return True

def find_brace(string):
    open_paran =  string.index('[')
    close_paran = string.index(']')
    if open_paran > close_paran:
        return False
    if (close_paran - open_paran) % 2 == 1:
        return True


print(valid_braces('(()')) 


