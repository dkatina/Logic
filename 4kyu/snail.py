def snail(snail_map):
    output = []
    while snail_map:
        for i in range(len(snail_map)):
            if i == 0:
                for num in snail_map[i]:
                   
                    output.append(num)
                    
                    
            elif i == len(snail_map) - 1:
                for num in snail_map[i][::-1]:
                    output.append(num)
                    
            else:
                output.append(snail_map[i].pop())
        if snail_map:
            del snail_map[0]
        if snail_map:
            del snail_map[-1]
        if snail_map:
            for array in snail_map[::-1]:
                output.append(array.pop(0))
    return output


arr = [[1,2,3],[4,5,6],[7,8,9]]

print(snail(arr))

# output = []
#     for i in range(len(snail_map)):
#         if i == 0:
#             for num in snail_map[i]:
#                 print(num)
#                 output.append(num)
#                 print(output)
#         elif i == len(snail_map) - 1:
#             for num in snail_map[i][::-1]:
#                 output.append(num)
#         else:
#             output.append(snail_map[i][-1])
#     return output

[[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10], 
[11, 12, 13, 14, 15], 
[16, 17, 18, 19, 20], 
[21, 22, 23, 24, 25]]