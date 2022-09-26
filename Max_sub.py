
def max_sequence(a_list):
    big_sum = a_list

    left = 0
    right = len(a_list) - 1

    while left <= right:
        