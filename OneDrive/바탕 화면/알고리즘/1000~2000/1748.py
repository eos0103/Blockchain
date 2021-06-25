item = int(input())
ctr = 1
sum = 0
while(item / 10**ctr >= 10):
    ctr+=1 
ctr += 1
for i in range(ctr):
    if(i == ctr-1):
        sum+=(item-10**ctr)*(ctr+1) 
    else:
        sum+=(ctr+1)*9*(10**i)
        print(sum)
print(sum)
