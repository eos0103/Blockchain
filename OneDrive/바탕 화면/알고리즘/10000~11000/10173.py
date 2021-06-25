ctr = 0
while(True):
    items = list(input())
    for i in range(len(items)):
        items[i] = items[i].upper()
    items = "".join(items).split(" ")
    if(items[0] == "EOI"):
        break
    for i in range(len(items)):
        if(items[i] == "NEMO" or items[i] == "NEMO,"):
            ctr += 1
    if(ctr > 0):
        print("Found")
    else:
        print("Missing")
    ctr = 0 