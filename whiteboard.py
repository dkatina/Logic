# Consecutive Indices
# You are given a list of unique integers (arr), and two integers (a and b). Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.
# Example:
# Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)
# Output: True
# Input: ([3,1,0,19], 19, 0)
# Output: True

#taking int a list and int a and int b

#fin the index of a
#find the index of b

# see if the index of a is before or after the index of b
#if so return True

#if not return False

# index_a = a_list.index(a)
#     index_b = a_list.index(b)
#     if index_a == index_b - 1 or index_a == index_b + 1:
#         return True
#     else:
#         return False

# a_list.index(a) == a_list.index(b) -1 or a_list.index(a) == a_list.index(b) +1

def consec_ind(a_list, a, b):
    return abs(a_list.index(a) - a_list.index(b)) == 1

    
