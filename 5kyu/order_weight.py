def order_weight(strng):
    print(strng)
    alist = strng.split()
    tupholder = []
    for weight in alist:
        hlist = []
        x = 0
        print(weight)
        for number in weight:
            x += int(number)
            print(x)
        hlist.append(weight)
        hlist.append(x)
        print(hlist)
        tupholder.append(hlist)
    print(tupholder)
    blist = sorted(tupholder, key=lambda x: (x[-1], x))
    print(blist)
    clist = []
    for list in blist:
        clist.append(list[0])
    print(clist)
    # return ' '.join(clist)

order_weight('103 123 4444 99 2000')