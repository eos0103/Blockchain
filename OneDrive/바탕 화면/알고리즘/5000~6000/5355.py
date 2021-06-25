for _ in range(int(input())):
    items = input().split()
    items[0] = float(items[0])
    for i in range(1, len(items)):
        if(items[i] == "@"):
            items[0] = items[0] * 3
        elif(items[i] == "%"):
            items[0] = items[0] + 5
        else:
            items[0] = items[0] - 7

    print("%.2f" %(items[0]))
