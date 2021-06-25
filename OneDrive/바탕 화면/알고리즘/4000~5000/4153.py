while(True):
    items = list(map(int, input().split()))
    items.sort()
    if(items[0] == 0 and items[1] ==0 and items[2] == 0):
        break
    if(items[0]**2 + items[1]**2 == items[2]**2):
        print("right")
    else:
        print("wrong")