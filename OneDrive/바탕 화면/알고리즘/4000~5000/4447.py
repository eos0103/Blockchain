for _ in range(int(input())):
    items = list(input())
    g_count = items.count("g")+items.count("G")
    b_count = items.count("b")+items.count("B")
    if(g_count > b_count):
        print("".join(items),"is GOOD")
    elif(g_count < b_count):
        print("".join(items),"is A BADDY")
    else:
        print("".join(items),"is NEUTRAL")