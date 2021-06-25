count = int(input())
items = []
for i in range(count):
    items.append(int(input()))
    if(i == count-1):
        last = items[i]
if(items[1] - items[0] == items[2] - items[1]):
    print(last+(items[1] -items[0]))
else:
    print(int(last*(items[1] / items[0])))