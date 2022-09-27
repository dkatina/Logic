def sum_of_intervals(intervals):
    
    output = []
    for i in range(len(intervals)):
        output+= list(range(intervals[i][0], intervals[i][1] + 1))
    return output

def sum_of_intervals(intervals):
    print(intervals)
    output = []
    for interval in intervals:
        output+= list(range(interval[0], interval[1]))
    return len(set(output))

def sum_of_intervals(intervals):
    print(intervals.sorted())
    
    output = 0
    for i in range(len(intervals)):
        intervals[i] = list(intervals[i])
    for interval in intervals:
        i = interval[1]
        for j in range(len(intervals)):
            if i > intervals[j][0] and i < intervals[j][1]:
                intervals[j][0] = i
    
    for interval in intervals:
        while intervals.count(interval) > 1:
            intervals.remove(interval)

    print('/n', intervals.sorted())
    for interval in intervals:
        output += abs(interval[1] - interval[0])
                
    print(output)
    return output
                
def sum_of_intervals(intervals):
    number = []
    maxn = 0
    minn = 0
    for i in intervals:
        if i[1] > maxn:
            maxn = i[1]
        if i[0] < minn:
            minn = i[0]
    for i in range(0, maxn - minn):
        number.append(0)
    for i in intervals:
        for j in range(i[0]-minn, i[1]-minn):
            number[j] = 1   
    return sum(number)

def sum_of_intervals(intervals):
    if not intervals:
        return 0
    def merge_intervals(intervals):
        intervals.sort()
        res = []
        start, end = intervals[0][0], intervals[0][1]
        
        for i, interval in enumerate(intervals[1:]):
            s, e = interval[0], interval[1]
            if s > end:
                res.append([start, end])
                start, end = s, e
            else:
                end = max(e, end)
        res.append([start, end])
        return res
            
        
    intervals = merge_intervals(intervals)
    res = 0
    for s, e in intervals:
        res += e - s
        
    return res