# Electric Company
# Create a function that given a list which represents street lights given as 
# a parameter(l_street), determine if an outage has occurred. A street with a 
# total number of “F” greater than or equal to 2 returns “Outage”, anything below
# returns “Power”
# Example Input: [ ‘T’, ‘F’, ‘F’, ‘F’ ]
# Example Output: “Outage”

def its_electric(alist):
    return 'outage' if alist.count('F') >= 2 else 'power'

print(its_electric(['T', 'T', 'F', 'F' ]))