for _ in range(int(input())):
    items = str(format(int(input()),'b'))
    # print(items)
    ctn = 0
    for i in range(len(items)-1, -1, -1):
        # print("==", items[i])
        if(items[i] == "1"):
            ctn = ctn + 1
            print(len(items)-1-i, end=" ")