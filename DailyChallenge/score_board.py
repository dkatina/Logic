def score_board(scores):
    output = [None for score in scores]
    a_dict = {}
    for index, score in enumerate(scores):
        a_dict[score] = index

    count = 1
    while a_dict:
        top = max(a_dict)
        if count == 1:
            output[a_dict[top]] = 'Gold Medal'
            del a_dict[top]
        elif count == 2:
            output[a_dict[top]] = 'Silver Medal'
            del a_dict[top]
        elif count == 3:
            output[a_dict[top]] = 'Bronze Medal'
            del a_dict[top]
        else:
            output[a_dict[top]] = f'{count}'
            del a_dict[top]
        count += 1
    return output

    
print(score_board([10,3,8,9,4,6]))

def placements(scores):
    placements = dict()
    sorted_scores = sorted(scores[:], reverse=True)
    
    placements[sorted_scores[0]] = 'Gold Medal'
    placements[sorted_scores[1]] = 'Silver Medal'
    placements[sorted_scores[2]] = 'Bronze Medal'
    
    for i, score in enumerate(sorted_scores[3:]):
        placements[score] = i+4
    return [placements[score] for score in scores]

print(placements([10,3,8,9,4,6]))