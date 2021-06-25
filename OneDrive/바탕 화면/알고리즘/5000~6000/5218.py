for _ in range(int(input())):
    item_a, item_b = input().split()
    items_a = list(map(ord, list(item_a)))
    items_b = list(map(ord, list(item_b)))
    line = []
    for i in range(len(items_a)):
        if(items_a[i] > items_b[i]):
            line.append(24 - abs(items_a[i] - items_b[i])+2) 
        else:
            line.append(abs(items_a[i] - items_b[i]))
    print("Distances:"," ".join(list(map(str,line))))
    line.clear()
