def max_points(points):
    slope= 0
    b= 0
    pot_slopes= []
    pot_b = []
    points = sorted(points, key=lambda x: x[0], reverse=False)
    
   
    p1 = 0
    p2 = len(points)-1    
    direction = 0
    finding_slope = True
    while finding_slope:
        m = (points[p2][1] - points[p1][1]) / (points[p2][0] - points[p1][0])
        if m in pot_slopes:
            slope = m
            finding_slope = False
        else:
            pot_slopes.append(m)
            if direction:
                p2 -= 1
                direction = 0
            else:
                p1 += 1
                direction = 1


    i = 0
    finding_b = True
    while finding_b:
        intercept = points[i][1] - (slope*points[i][0])
        if intercept in pot_b:
            b = intercept
            finding_b = False
        else:
            pot_b.append(intercept)
            i+=1
    
    points_on_line = 0
    for point in points:
        if point[1] == (slope*point[0]) + b:
            points_on_line += 1

    return points_on_line


print(max_points([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))