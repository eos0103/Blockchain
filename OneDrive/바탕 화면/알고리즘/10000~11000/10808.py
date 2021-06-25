items = list(input())
ctr = 0
for j in range(97, 123):
    for i in range(len(items)):
        if(items[i] == chr(j)):
            ctr +=1
        
    if(ctr >= 1):
        print(ctr, end=" ")
    else:
        print("0", end=" ")
    ctr = 0