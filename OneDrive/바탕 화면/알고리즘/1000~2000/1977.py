min = int(input())
max = int(input())
sum = 0
items = []
for i in range(1, 10000+1):
    if(min <= i**2 <= max):
        sum += i**2
        items.append(i**2)

if(len(items) == 0):
    print(-1)
else:
    print(sum)
    print(items[0])