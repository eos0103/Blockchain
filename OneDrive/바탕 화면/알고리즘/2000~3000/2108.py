sum = 0
c = []
g = {}
for i in range(int(input())):
    a = int(input())
    sum+=a
    c.append(a)
c = sorted(c)
for i in range(len(c)):
    try:
        g[c[i]] += 1
    except:
        g[c[i]] = 1

print()
print("adsd",max(g))
print(sum//len(c))
print(c[len(c)//2])
print()
print(max(c)-min(c))