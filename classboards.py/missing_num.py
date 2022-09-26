# You are given a list of numbers and a second list which is a scrambled version of the
# of the first list. Here is the kicker you number may be missing. Your job is to return
#  the missing number or 0 if both lists contain all the same numbers.

# if there are repeating number
def missing_num(alist, blist):
    for i in range(len(alist)):
        if alist[i] in blist:
            index = blist.index(alist[i])
            blist[index] = 'bop'
        else:
            return alist[i]
    return 0

print(missing_num([1,2,3,4,5], [3,4,1,5]))

# if there are not repeating numbers

def missing_num2(alist, blist):
    return sum(alist) - sum(blist)
print(missing_num2([1,2,3,4,5], [3,4,1,5]))