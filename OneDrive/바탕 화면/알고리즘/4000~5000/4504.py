compare_item = int(input())
while(True):
    item = int(input())
    if(item == 0):
        break
    if(item % compare_item == 0):
        print(item,"is a multiple of",compare_item,end="")
        print(".")
    else:
        print(item,"is NOT a multiple of",compare_item,end="")
        print(".")

    