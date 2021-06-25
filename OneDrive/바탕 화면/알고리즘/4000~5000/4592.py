while(True):
    items = list(map(int, input().split()))
    if(items[0] == 0):
        break
    # line = []
    i = 1
    ctn = 0
    while(True):
        ctn +=1
        if(ctn == 10):
            break
        if(i == len(items)):
            break
        if(items[i] == items[i+1]):
            print(items[i], end=" ")
            while(True):
                try:
                    if(items[i] == [i+1]):
                        i+=1
                    else:
                        break
                except:
                    pass
        else:
            print(items[i], end=" ")
            i+=1
    # print(" ".join(list(map(str, line)))+" $")