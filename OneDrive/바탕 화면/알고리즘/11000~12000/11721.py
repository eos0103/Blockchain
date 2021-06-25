items = list(input())
ctr = 1
if(len(items) < 10):
    print("".join(items))
else:
    for i in range(len(items)):
        print(items[i],end="")
        ctr += 1
        if(ctr == 11):
            print()
            ctr = 1