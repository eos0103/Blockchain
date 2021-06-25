while(True):
    item_a, item_b = map(int, input().split())
    if(item_a==0 & item_b==0):
        break
    if(item_a > item_b):
        print("Yes")
    else:
        print("No")
