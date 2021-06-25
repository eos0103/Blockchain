items = []
for i in range(5):
    items.append(sum(list(map(int, input().split()))))
value = items.index(max(items))
print(value+1, max(items))