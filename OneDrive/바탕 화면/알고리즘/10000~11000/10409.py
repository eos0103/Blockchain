item_a, item_b = map(int, input().split())
items = list(map(int, input().split()))
sum = 0
ctr = 0
for i in range(item_a):
    # print(1)
    sum += items[i]
    # print(sum)
    if(sum > item_b):
        # print(2)
        break
    else:
        ctr +=1
print(ctr)