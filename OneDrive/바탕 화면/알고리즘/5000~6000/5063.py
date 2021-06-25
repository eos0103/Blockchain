for  _ in range(int(input())):
    items = list(map(int, input().split()))
    if(items[0] < items[1] - items[2]):
        print("advertise")
    elif(items[0] == items[1] - items[2]):
        print("does not matter")
    else:
        print("do not advertise")