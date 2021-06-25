items = list(map(int, list(input())))
ctr = 0
while(len(items)!=1):
    items = list(map(int, list(str(sum(items)))))
    ctr +=1
if(items[0]%3 == 0):
    print(ctr)
    print("YES")
else:
    print(ctr)
    print("NO")