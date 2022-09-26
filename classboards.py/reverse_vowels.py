# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

def reverse_vowels(string):
    vowels = {'a','e','i','o','u'}
    my_vowels= []
    letters = []
    for letter in string:
        if letter in vowels:
            my_vowels.append(letter)
            letters.append("vowel")
        else:
            letters.append(letter)
    return ''.join(my_vowels.pop() if letter == 'vowel' else letter for letter in letters)

print(reverse_vowels('leetcode'))
