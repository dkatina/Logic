# Given a number return the closest number to it that is divisible by 10.
# Example input:
# 22
# 25
# 37
# Expected output:
# 20
# 30
# 40

def return_ten(number):
    
    return ((number // 10)*10)+10 if number % 10 >= 5 else (number // 10)*10

print(return_ten(345.5))








def return_ten2(number):

    number = str(number)
    last_dig = int(number[-1])
    add = 0
    if last_dig >= 5:
        add = 10 - last_dig
        return int(number) + add
    else:
        return int(number) - last_dig

print(return_ten2(343))
