first, mul = map(int, input().split())
items = []
val = first
cnt = 0
len_ctn = 0
temp = 0
while(True):
    cnt += 1
    val = str(val)
    for i in range(len(val)):
        temp += int(val[i])* mul
    val = temp
    items.append(val)
    temp = 0 
    if(cnt % 10 == 0 and len_ctn == len(items)):
        print(len_ctn)
    else:
        len_ctn = len(items)
        

