a = []
for i in range(1, 51):
    for _ in range(i):
        a.append(i)
a = sorted(a)
c, b = map(int, input().split())
print(sum(a[c-1:b]))