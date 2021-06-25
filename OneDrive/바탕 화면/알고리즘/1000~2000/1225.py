a, b = input().split()
a = list(map(int, a))
b = list(map(int, b))
sum_b = 0
b = sum(b)
for i in range(len(a)):
    sum_b+= b * a[i] 
print(sum_b)