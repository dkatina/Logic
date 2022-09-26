# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

def square_every_digit(number):
    # squared_nums = ''
    # for num in str(number):
    #     squared_nums += str( int(num)**2)
    # return squared_nums

    return int(''.join([str(int(num)**2) for num in str(number)]))
    
print(square_every_digit(9119))