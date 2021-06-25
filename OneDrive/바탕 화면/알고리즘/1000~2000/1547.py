items = [1, 2, 3]
# items[0] = items[0].replace("1", "4")
# print(items)
for _ in range(int(input())):
    a, b = map(int, input().split())
    temp = items[a-1]
    items[a-1] = items[b-1]
    items[b-1] = temp
print(items.index(1)+11)