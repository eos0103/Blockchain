items = []
max_items = []
max_indexes = []
max = 0
max_index = 0
for i in range(8):
    items.append(int(input()))
for _ in range(8):
    for i in range(8):
        if(max < items[i]):
            max = items[i]
            max_index = i+1
            items[i] = 0
    max_items.append(max)
    max_indexes.append(max_index)
    max = 0
print(max_items)
print(max_indexes)