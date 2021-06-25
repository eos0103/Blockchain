dic_items = {}
sum = 0
for i in range(10):
    item = int(input())
    sum += item
    try:
        dic_items[item] += 1
    except:
        dic_items[item] = 1
max_item = 0
for key, value in dic_items.items():
    if(max_item < value):
        max_item = value
        max_key = key 
print(int(sum/10))
print(max_key)