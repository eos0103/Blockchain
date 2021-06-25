a = []
g = []
count = int(input())
for _ in range(count):
    a.append(*list(input())[:1])
c =list(set(a))
for i in range(len(c)):
    if (a.count(c[i]) >= 5):
        g.append(c[i])
if g == []:
    print("PREDAJA")
else:
    print("".join(sorted(g)))