# Write a functin which takes a list and return the biggest number that occurs only
# once. If there are no such numbers return -1

def big_one(alist):
    while True:
        if not alist:
            return -1
        my_max = max(alist)
        if alist.count(my_max) > 1:
            alist = list(filter(lambda num: num != my_max, alist))
        else:
            return my_max
    
test = [1,1,1]   
print(big_one(test))