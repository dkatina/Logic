# # Given an array of integers nums sorted in non-decreasing order, 
# # find the starting and ending position of a given target value.
# # If target is not found in the array, return [-1, -1].
# # Example 1:
# # Input: nums = [5,7,7,8,8,10], target = 8
# # Output: [3,4]
# # Example 2:
# # Input: nums = [5,7,7,8,8,10], target = 6
# # Output: [-1,-1]
# # Example 3:
# # Input: nums = [], target = 0
# # Output: [-1,-1]

# def start_end(nums, target):
#     if target not in nums:
#         return [-1,-1]
    
#     start = nums.index(target)
#     end = start
#     output = [start, end]
#     while nums[end + 1] == target:
#         end += 1
#         output[1] = end
        
#     return output

# def start_end2(nums, target):
#     if target not in nums:
#         return [-1,-1]
    
#     start = nums.index(target)
#     end = (len(nums) - 1) - nums[::-1].index(target)
#     output = [start, end]
    
        
#     return output


# print(start_end2([5,7,7,8,8,10], 6))

# # def start_end3(nums, target):
# #     left = 0
# #     right = len(nums) - 1

# #     while nums[left] != target or nums[right] != target:
# #         if nums[left] != target and nums[right] != target:
# #             left += 1
# #             right -= 1
# #         elif nums[left]

# def start_end4(nums, target):
#     left_i = (len(nums) - 1) // 2
#     left = left_i
#     l_nums = nums[:]
#     right_i = (len(nums) - 1) // 2
#     r_nums = nums[:]
#     while nums[left] != target and nums[left - 1] < target: 
#         if nums[left] == target:
#             while nums[left - 1] == target:
#                 left -= 1
#         if l_nums[left_i] < target:
#             l_nums = l_nums[left_i:]
#             left_i = (len(nums) - 1) // 2
#             left += left_i
#             print(l_nums, left)
#         else:
#             l_nums = l_nums[:left_i]
#             left_i = (len(nums) - 1) // 2
#             left -= left_i
#             print(l_nums, left)
        

#     return left

# print(start_end4([5,7,7,8,8,10], 8))

def start_end5(nums, target):
   
    i = (len(nums) - 1) // 2
    print(i)
    y = i
    search_nums = nums[:]

    while search_nums[i] != target:
        print(i)
        if search_nums[i] < target:
            search_nums = search_nums[i+1:]
            i = (len(search_nums) - 1) // 2
            y += i

        else:
            search_nums = search_nums[:i]
            i = (len(search_nums) - 1) // 2
            y += i

        if len(search_nums) == 1 and search_nums[i] != target:
            return [-1,-1]
    
    right = y
    while nums[right+1] == target:
        right += 1

    left = y
    while nums[left-1] == target:
        left-= 1
    
    return [left, right]

    
    

    

print(start_end5([5,7,7,8,8,10], 6))
