items = input().split("_")
if(len(items) == 1):
    for i in range(len(items[0])):
        if(items[0][i].isupper()):
            print("_"+items[0][i],end="")
        else:
            print(items[0][i],end="")
else:
    print("".join(items))

