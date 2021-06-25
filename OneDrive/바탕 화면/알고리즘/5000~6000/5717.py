while(True):
    item_a, item_b = map(int, input().split())
    if(item_a == 0 and item_b == 0):
        break
    else:
        print(item_a + item_b)