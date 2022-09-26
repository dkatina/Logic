# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions 
# were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, 
# "WEST" and "EAST" too.
# Going to one direction and coming back the opposite direction right away is a
#  needless effort. Since this is the wild west, with dreadful weather and not
#  much water, it's important to save yourself some energy, otherwise you might
#  die of thirst!
# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on
#  the language):
# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]
# You can immediately see that going "NORTH" and immediately "SOUTH" is not 
# reasonable, better stay to the same place! So the task is to give to the man
#  a simplified version of the plan. A better plan in this case is simply:
# ["WEST"]
# or
# { "WEST" }
# or
# [West]

#given directions as a list
#Read through directions
#determin if next direction is opposite 
#If so ignore current direction and next direction

#while n > mylist
#if mylist[n+1] is opposite mylist[n]
 #n+=2
#else:
    #new_direc.append(mylist[n])
    #n +=1




def simply_direct(alist):
    new_direct = []
    n = 0
    opposites = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }
    while n < len(alist):
        if n == len(alist)-1:
            if new_direct:
                if new_direct[-1] == opposites[alist[n]]:
                    del new_direct[-1]
            else:
                new_direct.append(alist[n])
            n +=1
        elif alist[n+1] == opposites[alist[n]]:
            n+=2
        elif new_direct:
            if new_direct[-1] == opposites[alist[n]]:
                del new_direct[-1]
            else:
                new_direct.append(alist[n])
            n += 1
        else:
            new_direct.append(alist[n])
            n+=1
        
    return new_direct
    
print(simply_direct(["NORTH", "SOUTH", "SOUTH", "EAST",'WEST', "WEST", "NORTH", "WEST"]))