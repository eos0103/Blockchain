while(True):
    items = input().split()
    if(items[0] == "#"):
        break
    else:
        value = items[0]
        items[0] = items[0].upper()
        count = 0
        print(items, items[0])
        for i in range(len(items)):
            items[i] = items[i].upper()
            for i in range(1,len(items)-1):
                count = items[i].count(items[0])
        print(value, count)