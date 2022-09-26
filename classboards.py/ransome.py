# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# ransomNote2 = "a"
# magazine2 = "b"
# Output: false
# Example 2:
# ransomNote1 = "aa"
# magazine1 = "ab"
# Output: false
# Example 3:
# ransomNote = "aa"
# magazine = "aab"
# Output: true
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

def ransomNote(ransom, magazine):
    mag = list(magazine)
    return True if False not in [mag.remove(letter) if letter in mag else False for letter in ransom] else False

print(ransomNote("aa", "aab"))
