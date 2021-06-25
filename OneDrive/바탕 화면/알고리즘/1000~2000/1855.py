cnt = int(input())
items = list(input())
formally_items = []
# temporary_items = []
for i in range(len(items)//cnt):
    if(i % 2 != 0):
        formally_items.append(list(reversed(items[i*3:(i+1)*3])))
    else:
        formally_items.append(items[i*3:(i+1)*3])
# print(formally_items[3][2])
for j in range(cnt):
    for i in range(len(formally_items)):
        print(formally_items[i][j], end="")