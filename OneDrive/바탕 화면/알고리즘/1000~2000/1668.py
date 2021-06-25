count = int(input())
left_max = 1
left_ctr = 1
right_max = 1
right_ctr = 1
items = []
for _ in range(count):
    items.append(int(input()))
left_max = items[0]
for i in range(1, count):
    if(left_max < items[i]):
        left_max = items[i]
        left_ctr +=1
right_max = items[len(items)-1]
for j in range(count-1,-1,-1):
    if(right_max < items[j]):
        right_max = items[j]
        right_ctr +=1
print(left_ctr)
print(right_ctr)
