count = int(input())
item = list(map(int, input().split()))
ctr = []
length = 1
try:
    for i in range(count-1): 
        if(item[i]<= item[i+1]):
            length += 1
        else:
            ctr.append(length) 
            length = 1
    print(max(ctr))
except:
    print(1)
