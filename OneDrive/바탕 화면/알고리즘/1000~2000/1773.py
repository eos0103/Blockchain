import math
std_cnt, time = map(int, input().split())
sum = 0
for _ in range(std_cnt):
    sum += math.floor(time/int(input()))
    print(sum)
print(sum)