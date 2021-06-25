ctr =0
count = int(input())
a = list(map(int, input().split()))
for j in range(count):
    if (a[j]<3):
        pass
    else:
        b = 0
        for i in range(2, a[j]):
            if a[j]%i==0:
                b=1
        if b==0:
            ctr+=1
print(ctr)