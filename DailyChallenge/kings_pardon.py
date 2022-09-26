# Last Man Standing
# A king gathers all the men in the kingdom who are to be put to death for their
#  crimes, but because of his mercy, he will pardon one. He gathers the men into
#  a circle and gives the sword to one man. The man kills the man to his left,
#  and gives the sword to the man to the dead man's left. The last man alive is
#  pardoned. 

# With 5 men, the 3rd man holding the sword is the last man alive. 

# Write a program that accepts a single parameter: a number N that represents
#  the number of criminals to start with. The program should output the number
#  of the last two men alive.

# Example #1: myProgram 5

# would output:

# 5, 3

# Example #2: myProgram 7

# would output:

# 3, 7

# criminals = 7
# line = [1, 2, 3, 4, 5, 6, 7]

def kings_pardon(criminals):
    line = list(range(1,criminals+1))
    holder = 1
    while len(line) > 2:
        print(line)
        print(holder)
        if holder == line[len(line) - 2]:
            del line[-1]
            holder = line[0]
        elif holder == line[len(line) - 1]:
            del line[0]
            holder = line[0]
        else:
            del line[line.index(holder)+1]
            holder = line[line.index(holder)+1]
    return line

print(kings_pardon(5))