count = int(input())
item = []
dump = 0
move = 0
for i in range(1, count+1):
    item.append(i)
while(len(item)!=1):
    item.remove(item[0])
    move = item[0]
    item.remove(move)
    item.append(move)
print(item[0])