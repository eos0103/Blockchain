while(True):
    items = list(map(int, input().split()))
    if(items[0] == 0 and items[1] == 0 and items[2] == 0 and items[3] == 0):
        break
    cnt = 0
    sign = 0
    while(True):
        if(sign == 10):
            break
        sign +=1
        if(items[0] == items[1] == items[2] == items[3]):
            print(cnt)
            cnt = 0
            break
        # print(items[2],items[3])
        temp = items[0]
        for i in range(3):
            if (items[i] - items[i+1] < 0):
                items[i] = (items[i] - items[i+1])*-1
            else:
                items[i] = items[i] - items[i+1]
        if(items[3] - temp < 0):
            items[3] = (items[3] - temp) * -1
        else:
            items[3] = items[3] - temp
        # print(items)
        cnt +=1 
