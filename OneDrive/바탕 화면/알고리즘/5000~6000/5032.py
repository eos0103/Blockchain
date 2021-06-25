count, rec, chg_ctn  = map(int, input().split())
count = count + rec
sum = 0
ctn = 0
while(True):
    if(count // chg_ctn < 1):
        break
    sum += count // chg_ctn
    ctn += sum
    rem_ctn = count % chg_ctn
    count = sum
    count += rem_ctn
    sum = 0
    # print(count)
print(ctn)