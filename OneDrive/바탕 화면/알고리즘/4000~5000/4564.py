while(True):
    items = list(input())
    if(items[0] == "0"):
        break
    sum = 1
    print("".join(items), end=" ")
    while(True):
        if(len(items) == 1):
            print()
            break
        else:
            items = list(map(int, items))
            for i in range(len(items)):
                sum *= items[i]
            print(sum, end=" ")
            items = list(str(sum))
            sum = 1