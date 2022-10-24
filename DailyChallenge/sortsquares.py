def solve(A):
        length = len(A) -1 
        negatives = []
        for i in range(len(A)):
            if A[i] < 0:
                negatives.append(A[i])
            
        positives = A[len(negatives):]
        print(negatives)
        print(positives)
        output= []
        count = 0
        n = len(negatives) - 1
        p = 0
        while count < length:
            if n == 0:
                output.append(positives[p]**2)
                p += 1
                count += 1
            elif p == len(positives) - 1:
                output.append(negatives[n]**2)
                n -= 1
                count += 1
            else:
                if negatives[n]**2 > positives[p]**2:
                    output.append(positives[p]**2)
                    p += 1
                    count += 1
                elif negatives[n]**2 < positives[p]**2:
                    output.append(negatives[n]**2)
                    n -= 1
                    count += 1
                else:
                    output.append(negatives[n]**2)
                    output.append(positives[p]**2)
                    n -= 1
                    p += 1
                    count += 2
        print(output)
        return output

A = [ -979, -959, -947, -873, -776, -719, -709, -697, -691, -690, -657, -650, -582, -579, -533, -517, -516, -515, -481, -477, -404, -400, -391, -383, -352, -298, -266, -202, -187, -164, -107, -100, -65, -11, 8, 20, 93, 195, 199, 249, 348, 374, 451, 514, 556, 587, 602, 616, 668, 728, 788, 807, 844, 938, 999 ]

print(solve(A))