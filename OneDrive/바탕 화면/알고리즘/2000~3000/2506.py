count = int(input())
items = list(map(int, input().split()))
sum = 0
ctr = 0
for i in range(count):
    if(items[i] == 1):
        ctr += 1
        sum += ctr
    else:
        ctr = 0
print(sum)