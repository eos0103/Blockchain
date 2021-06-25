items = input().split(":")
# print(items)
for i in range(len(items)):
    try:
        print("%04d" %(int(items[i])),end="")
        # print("check",items[i], end="??")
    except:
        cnt = len(items[i])
        tem = items[i]
        for j in range(cnt):
            print("0",end="")
        print(tem,end="")
    if(i == len(items)-1):
        break
    else:
        print(":",end="")