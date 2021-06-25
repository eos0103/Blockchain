max_val = 0
for _ in range(int(input())):
    items = list(map(int, input().split()))
    if(items[0] == items[1] == items[2] == items[3]):
        value = 50000 + 5000*items[0]
    else:
        if(items[0] == items[1] == items[2] or items[0] == items[1] == items[3] or items[1] == items[2] == items[3]):
            if(items[0] == items[1] == items[2]):
                value = 10000 + items[0]*1000
            if(items[0] == items[1] == items[3]):
                value = 10000 + items[0]*1000
            if(items[1] == items[2] == items[3]):
                value = 10000 + items[1]*1000 
        else:
            if(items[0] == items[1] or items[0] == items[2] or items[0] == items[3] or items[1] == items[2] or items[1] == items[3] or items[2] == items[3]):
                if(items[0] == items[1]):
                    value = 2000 + items[1] * 500 + items[2] * 500
                elif(items[0] == items[2]):
                    value = 2000 + items[1] * 500 + items[3] * 500
                elif(items[0] == items[3]):
                    value = 2000 + items[0] * 500 + items[1] * 500
                elif(items[1] == items[2]):
                    value = 2000 + items[1] * 500 + items[3] * 500
                elif(items[1] == items[3]):
                    value = 2000 + items[1] * 500 + items[2] * 500
                elif(items[2] == items[3]):
                    value = 2000 + items[1] * 500 + items[2] * 500
            else:
                value = 100 * max(items)
    if(value > max_val):
        max_val = value
print(max_val)
    