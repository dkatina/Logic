def sum_of_intervals(intervals):
    
    output = []
    for i in range(len(intervals)):
        output+= list(range(intervals[i][0], intervals[i][1] + 1))
    return output
