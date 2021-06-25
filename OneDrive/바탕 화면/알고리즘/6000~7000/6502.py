ctn = 1
while(True):
    items = list(map(int, input().split()))
    if(items[0] == 0):
        break
    if(min(items) == items[0]):
        print("Pizza",ctn,"fits on the table.")
    else:
        print("Pizza",ctn,"does not fit on the table.")
    ctn += 1
