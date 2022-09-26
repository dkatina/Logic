
def  roman(string):
    rv = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    last = 0
    number = 0
    for char in string[::-1]:
        if rv[char] < last:
            number -= rv[char]
        else:
            number += rv[char]
        last = rv[char]
    return number

print(roman('MMXI'))
        
def to_roman(val):
    thousands = val// 1000
    hundreds = val % 1000 // 100
    tens = val % 100 // 10
    ones = val % 10
    roman +=  'M'*thousands
    if hundreds == 9:
        roman += 'CM'
    elif hundreds >= 5:
        roman += 'D' + 'C'*(hundreds - 5)
    elif hundreds < 4:
        roman += 'C'*hundreds
    else: 
        roman += 'CD'
    
    if tens == 9:
        roman += 'XC'
    elif tens >= 5:
        roman += 'L' + 'X'*(tens - 5)
    elif tens < 4:
        roman += 'X'*tens
    else: 
        roman += 'XL'

    if ones == 9:
        roman += 'IX'
    elif ones >= 5:
        roman += 'V' + 'I'*(ones - 5)
    elif ones < 4:
        roman += 'I'*ones
    else: 
        roman += 'IV'
