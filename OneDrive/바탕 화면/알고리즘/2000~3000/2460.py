sum = 0
max = 0
for _ in range(10):
    down, up = map(int, input().split())
    sum -= down
    sum += up
    if(max < sum):
        max = sum
print(max)
