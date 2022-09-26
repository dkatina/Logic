


from re import T


def leave_or_stay(dict, boss):
    total_happiness = 0
    for key, value in dict.items():
        if key == boss:
            total_happiness += value*2
        else:
            total_happiness += value

    total_happiness /= len(dict)

    return 'Get Out Now!' if total_happiness <= 5 else 'Nice Work Champ!'
