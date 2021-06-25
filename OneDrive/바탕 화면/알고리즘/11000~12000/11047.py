cnt, price = map(int, input().split())
items = []
c = 0
for i in range(cnt):
    items.append(int(input()))
while(price != 0):
    for j in range(cnt):
        if(price // items[cnt-j-1] >= 1):
            # print(items[cnt-j-1], price, end="?? ")
            # print(c)
            c += price // items[cnt-j-1]
            price = price % items[cnt-j-1]
            
        else:
            pass
print(c)