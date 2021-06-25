while(True):
    items = list(input())
    if(items[0] == "#"):
        break
    if(items[len(items)-1] == "e"):
        ctn = items.count("1")
        if(ctn % 2 == 0):
            items[len(items)-1] = "0"
        else:
            items[len(items)-1] = "1"
    else:
        ctn = items.count("1")
        if(ctn % 2 == 1):
            items[len(items)-1] = "0"
        else:
            items[len(items)-1] = "1"
    print("".join(items))
