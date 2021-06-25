for i in range(3):
    items = list(map(int, list(input())))
    ctr = 1
    max_ctr = 1
    for i in range(len(items)-1):
        # print(items[i], items[i+1])
        if(items[i] == items[i+1]):
            ctr+=1
        else:
            ctr = 1
        if(max_ctr < ctr):
            max_ctr = ctr
    print(max_ctr)