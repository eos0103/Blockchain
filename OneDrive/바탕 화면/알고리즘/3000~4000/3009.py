items = []
complete_items = []
sum = 0
for _ in range(3):
    item_a, item_b = map(int, input().split())
    items.append(item_a)
    items.append(item_b)
set_items = list(dict.fromkeys(items))
for i in range(len(set_items)):
    if(items.count(set_items[i])%2==0):
        pass
    else:
        complete_items.append(set_items[i])
print(" ".join(list(map(str, complete_items))))