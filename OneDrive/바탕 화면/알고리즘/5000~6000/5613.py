items = []
sign = 0
while(sign != 1):
    item = input()
    if(item != "="):
        items.append(item)
    else:
        items.append(item)
        sign = 1
for i in range(0, len(items), 2):
    if(items[i+1] == "="):
        print(items[i])
    elif(items[i+1] == "+"):
        items[i+2] = int(items[i])+ int(items[i+2])
    elif(items[i+1] == "-"):
        items[i+2] = int(items[i])- int(items[i+2])
    elif(items[i+1] == "*"):
        items[i+2] = int(items[i])* int(items[i+2])
    elif(items[i+1] == "/"):
        items[i+2] = int(items[i])/ int(items[i+2])
        