items = [100, 100]
for _ in range(int(input())):
    a,b = map(int, input().split())
    if(a==b):
        pass
    else:
        if(a > b):
            items[1] = items[1]-a
        else:
            items[0] = items[0]-b
print(items[0])
print(items[1])