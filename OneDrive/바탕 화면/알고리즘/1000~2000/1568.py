count = int(input())
ctr = 0
value = 0
while(count != 0):
    
    value+=1
    if(value <= count):
        count -= value
        ctr +=1
    else:
        value = 1
        count -= value
        ctr +=1
print(ctr)
