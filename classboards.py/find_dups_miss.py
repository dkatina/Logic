# In this kata, we have an unsorted sequence of consecutive numbers from a to b,
#  such that a < b always (remember a, is
# the minimum, and b the maximum value). They were introduced an unknown amount 
# of duplicates in this sequence and we
# know that there is an only missing value such that all the duplicate values 
# and the missing value are between a and b,
# but never coincide with them. Find the missing number with the duplicate 
# numbers (duplicates should be output in a sorted array).
# Let's see an example:
# arr = [10,9,8,9,6,1,2,4,3,2,5,5,3]
# find_dups_miss([10,9,8,9,6,1,2,4,3,2,5,5,3]) == [7,[2,3,5,9]]
# The code should be fast to process long arrays 
# (maximum length aprox. = 1.000.000). The values for the randon tests:
# 500 <= a <= 50000
# a + k <= b and 100 <= k <= 1000000
# amount of duplicates variable, according to the length of the array

def find_dups_miss(array):
    print(array)
    my_set = list(set(array))
    print(my_set)
    my_start = min(my_set)
    my_end = max(my_set)
    total= sum(list(range(my_start,my_end+1))) - sum(my_set)
    print(total)
    print(my_set)
    print(array)
    output_list = []
    for num in my_set:
        print(num)
        print(array.count(num))
        if array.count(num) > 1:
            output_list.append(num)
    print(output_list)
   
    return  (total, output_list)

print(find_dups_miss([10,9,8,9,6,1,2,4,3,2,5,5,3]))