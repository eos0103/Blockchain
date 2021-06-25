item = []
ctr = 0
for j in range(1, 46):
    for _ in range(j):
        item.append(j)
a, b = map(int, input().split())
print(sum(item[a-1:b]))