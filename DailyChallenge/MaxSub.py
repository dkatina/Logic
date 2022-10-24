
#need to look at subarrays of the nums array, whose lengths are = k and return the 
#highest average derived from the sub   arrays



def max_sub(nums, k):
    left = 0
    right = k
    highest_avg = 0
    while right <= len(nums):
        avg = sum(nums[left:right])/k
        if avg > highest_avg:
            highest_avg = avg
        left += 1
        right += 1
    return highest_avg

print(max_sub([5],1))