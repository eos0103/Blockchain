d, n = map(int, input().split())
a = [False,False] + [True]*(n-1)
primes=[]
g = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for i in range(len(primes)):
    if(primes[i] < d):
        g.append(primes[i])
    else:
        break
for i in range(len(g)):
    primes.remove(g[i])

if primes == []:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))

# for i in range(len(primes)):
#     print(primes[i])