sum = 0
for _ in range(4):
    sum += int(input())
minute = sum//60
second = sum%60
print(minute)
print(second)