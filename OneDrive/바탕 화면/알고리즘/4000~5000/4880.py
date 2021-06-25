while(True):
    item_a, item_b, item_c = map(int, input().split())
    if(item_a == 0 and item_b == 0 and item_c == 0):
        break
    else:
        if((item_c - item_b) == (item_b - item_a)):
            print("AP", int(item_c + (item_c - item_b)))
        else:
            print("GP", int(item_c * (item_c/ item_b)))