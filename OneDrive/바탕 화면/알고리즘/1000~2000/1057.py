round, item_a, item_b = map(int, input().split())

items_ctr = []
ctr = 0
while(round != 0):
    round = round//2
    ctr +=1
items_ctr.append(ctr)
ctr = 0

if(item_a//2 !=0):
        ctr+=1
while(item_a != 0):
    item_a = item_a//2
    ctr +=1
items_ctr.append(ctr)
ctr = 0

if(item_b//2 !=0):
        ctr+=1
while(item_b != 0):
    item_b = item_b//2
    ctr +=1
items_ctr.append(ctr)
ctr = 0
print(items_ctr[0])
print(items_ctr[1])
print(items_ctr[2])
if(items_ctr[2] >= items_ctr[0] or items_ctr[1] >= items_ctr[0]):
    print("-1")
else:
    if(items_ctr[1] <= items_ctr[2]):
        print(items_ctr[2]-1)
    else:
        print(items_ctr[1]-1)
