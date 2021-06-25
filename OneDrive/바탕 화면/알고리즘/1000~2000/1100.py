a = []
ctr = 0
for _ in range(8):
    a.append(list(input()))
for i in range(2):
    if i % 2 == 0:
        for j in range(0,8,2):
            if(a[i][j] !="F"):
                ctr +=1
    else:
        for k in range(1,8,2):
            if(a[i][k] !="F"):
                ctr +=1
                print(1)
print(ctr)