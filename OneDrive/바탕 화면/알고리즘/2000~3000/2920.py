items = list(map(int, input().split()))
ctr = 0
ctr_b = 0
for i in range(7):
    if items[i] < items[i+1]:
        ctr +=1
    else:
        ctr_b+=1
if(ctr == 7):
    print("ascending")
elif(ctr_b == 7):
    print("descending")
else:
    print("mixed")