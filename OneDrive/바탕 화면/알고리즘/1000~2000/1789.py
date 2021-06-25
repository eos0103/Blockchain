item = int(input())
ctn = 0
sum = 0

while(True):
    if(item <= sum):
        break
    else:
        ctn += 1
        sum += ctn
        print(sum, ctn)
print(ctn)
    