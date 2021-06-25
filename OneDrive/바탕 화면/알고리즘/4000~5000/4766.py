import decimal
i = 0
while(True):
    item = float(input())
    if(item == 999.0):
        break
    if(i >= 1 ):
        cur = item
        print(round(item - cur, 5)) 
    else:
        cur = item
    i+=1