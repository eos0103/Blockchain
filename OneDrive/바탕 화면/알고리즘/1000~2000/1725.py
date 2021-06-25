items = []
for _ in range(int(input())):
    items.append(int(input()))
sum = 0
max_items = []
ctr = 0 
for i in range(1, len(items)):
    try:
        if(items[i]<items[i+1] and ctr >= 1):
            ctr +=1
            sum += 
        elif(items[i]<items[i+1]):
            +=
        else:
            max_items.append(sum)
            sum = 0
            ctr = 0 