ctn_a = int(input())
for k in range(ctn_a):
    ctn = int(input())
    for _ in range(ctn):
        print("#", end="")
    print()
    for j in range(ctn-2):
        if(ctn> 2):
            print("#",end="")
        for i in range(ctn-2):
            print("J", end="")
        if(ctn> 2):
            print("#")

    for _ in range(ctn):
        print("#", end="")
    print()
    if(k == ctn_a-1):
        pass
    else:
        print()