count, item_b = map(int, input().split())
items = []
for i in range(1, count+1):
    items.append(i)
while(True):
    if(len(items)==0):
        break
    try:
        count = len(items)//3
        del(items[(i*3)-1])
    except:
        count 