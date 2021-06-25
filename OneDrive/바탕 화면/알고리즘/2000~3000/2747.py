items = [0, 1]
for i in range(int(input())-1):
    items.append(items[i]+items[i+1])
print(items[len(items)-1])