def format_duration(seconds):
    if not seconds: return 'now'
    years = seconds // (3600*24*365)
    days = (seconds // (3600*24)) % 365
    hours = seconds // 3600 % 24
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time = []
    sentence = ''
    if years:
        time.append(f'{years} year{"s" if years > 1 else ""}, ')
    if days:
        time.append(f'{days} day{"s" if days > 1 else ""}, ')
    if hours:
        time.append(f'{hours} hour{"s" if hours > 1 else ""}, ')
    if minutes:
        time.append(f'{minutes} minute{"s" if minutes > 1 else ""}, ')
    if seconds:
        time.append(f'{seconds} second{"s" if seconds > 1 else ""}, ')
    
    for i in range(len(time)):
        if i == len(time) - 1 and i > 0:
            sentence = sentence.strip(' ,') + f' and {time[i]}'
        else:
            sentence += f'{time[i]}'
    return sentence.strip(' ,')

        





 


    if hours:
        if minutes:
            if seconds:
                return f'{hours} hour{"s" if hours > 1 else ""}, {minutes} minute{"s" if minutes > 1 else ""} and {seconds} second{"s" if seconds > 1 else ""}'
            else:
                return f'{hours} hour{"s" if hours > 1 else ""} and {minutes} minute{"s" if minutes > 1 else ""}'
        elif seconds:
            return f'{hours} hour{"s" if hours > 1 else ""} and {seconds} second{"s" if seconds > 1 else ""}'
        else:
            return f'{hours} hour{"s" if hours > 1 else ""}'
    elif minutes:
        if seconds:
            return f'{minutes} minute{"s" if minutes > 1 else ""} and {seconds} seconds{"s" if seconds > 1 else ""}'
        else:
            return f'{minutes} minute{"s" if minutes > 1 else ""}'
    else:
        return f'{seconds} seconds{"s" if seconds > 1 else ""}'

   

