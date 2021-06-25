while(True):
    item = int(input())
    if(item == 0):
        break
    else:
        while(True):
            item =sum(list(map(int, list(str(item)))))
            if(len(list(str(item))) <= 1):
                print(item)
                break
