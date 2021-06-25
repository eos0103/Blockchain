value = int(input())
items = [300, 60, 10]
ctr_items = [0, 0, 0]
if(value / 300 >= 1):
    ctr_items[0] = value // 300
    value = value % 300
if(value / 60 >= 1):
    ctr_items[1] = value // 60
    value = value % 60
if(value / 10):
    ctr_items[2] = value // 10
    value = value % 10
if(value != 0):
    print(-1)
else:
    for i in range(3):
        print(ctr_items[i], end=" ")

