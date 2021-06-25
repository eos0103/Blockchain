items = []
for _ in range(int(input())):
    item = int(input())
    try:
        if(item!=0):
            items.append(item)
        else:
            items.pop()
    except:
        pass
print(sum(items))