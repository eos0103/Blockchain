for _ in range(int(input())):
    items = list(map(int, list(input())))
    if(len(items)>=2):
        # print(items)
        for i in range(len(items)-1,-0,-1):
            if(items[i] >= 5):
                items[i] = 0
                items[i-1] += 1
            else:
                items[i] = 0
        print("".join(list(map(str, items))))
    else:
        print(items[0])