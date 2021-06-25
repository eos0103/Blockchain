try:
    sum = 0
    items = []
    for i in range(7):
        item = int(input())
        if(item %2 == 1):
            sum+=item
            items.append(item)
    print(sum)
    print(min(items))
except:
    print(-1)