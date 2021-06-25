
ctn = int(input())
for i in range(ctn):
    items = list(input())
    for j in range(len(items)):
        if(items[j] == "Z"):
            items[j] = "A"
        else:
            items[j] = chr(ord(items[j])+1)
    print("String #",end="")
    print(i+1)
    print("".join(list(map(str, items))))
    if(i != ctn-1):
        print()
    else:
        pass
