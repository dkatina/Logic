# In this kata, you will write a function that returns the positions and the 
# values of the "peaks" (or local maxima) of a numeric array.

# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 
# with a value of 5 (since arr[3] equals 5).

# The output will be returned as an object with two properties: pos and peaks. 
# Both of these properties should be arrays. If there is no peak in the given 
# array, then the output should be {pos: [], peaks: []}.

# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return 
# {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

# All input arrays will be valid integer arrays (although it could still be 
# empty), so you won't need to validate the input.

# The first and last elements of the array will not be considered as peaks 
# (in the context of a mathematical function, we don't know what is after and 
# before and therefore, we don't know if it is a peak or not).

# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] 
# and [1, 2, 2, 2, 2] do not. In case of a plateau-peak, please only return the 
# position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1])
# returns {pos: [1], peaks: [2]} (or equivalent in other languages)


#read through a list, probably want to enumerate to get the index of every value.
#Identify if the value before and after is are below
#If so this value is a peak and it's index should be appended to the list
#associated with the key 'pos' and the value should be appended to the list
#associated with the key 'peaks'

# Platue if the value after a value is the same this could be a platue, continue
# evaluating whether the the next value is the same until you the list runs out,
# or the next value is not the same, if the next is lower, you have run into a platue-peak
# return the first value that started the platue and its pos

#The first and last element in the list can't be platues

def pick_peaks(arr):
    output = {'pos': [], 'peaks': []}
    holder = {}
    for index, value in enumerate(arr):
        holder[index] = value
    i = 1
    while i < len(holder) - 1:
        plat = 0
        if holder[i-1] < holder[i] > holder[i+1]:
            output['pos'].append(i)
            output['peaks'].append(holder[i])

        elif  holder[i-1] < holder[i] == holder[i+1]:
            plat = i
            while holder[i] == holder[plat] and plat < len(holder) - 1:
                plat+=1
            if holder[i] > holder[plat]:
                output['pos'].append(i)
                output['peaks'].append(holder[i])
        i += 1
    return output


print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))

#Cool solution

def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i          #--stores i goes to next loop
        elif arr[i] < arr[i-1] and prob_peak:           
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}