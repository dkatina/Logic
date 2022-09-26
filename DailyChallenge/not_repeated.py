def repeatnums(nums):
    nums_dict = {}
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1
    for key in nums_dict:
        if nums_dict[key] == 1:
            return key

print(repeatnums([1,1,2,2,3]))


def func(nums):
    unique = 0
    for i in nums:
        unique = unique ^ i
    return unique

print(func([4,2,2]))