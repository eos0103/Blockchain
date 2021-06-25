items = list(input())
for i in range(len(items)):
    if(items[i].islower()):
        items[i] = items[i].upper()
    else:
        items[i] = items[i].lower()
print("".join(items))