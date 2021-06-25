days, seq = map(int, input().split())
items = list(map(int,input().split()))
sum = 0
max = -123123
for i in range(days):
    try:
        sum += items[i]
        for j in range(1, seq):
            sum += items[i+j]
        if(max < sum):
            max = sum
        sum = 0
    except:
        pass
print(max)
