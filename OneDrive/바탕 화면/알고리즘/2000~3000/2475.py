a = list(map(int, input().split()))
sum = 0
for i in range(len(a)):
    sum += pow(a[i], 2)
print(sum % 10)