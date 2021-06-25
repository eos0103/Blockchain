item_a, item_b,  item_c = map(int, input().split())
if((item_a + item_b) ==item_c):
    print(item_a,end="")
    print("+",end="")
    print(item_b,end="")
    print("=",end="")
    print(item_c,end="")
elif((item_a - item_b) ==item_c):
    print(item_a,end="")
    print("-",end="")
    print(item_b,end="")
    print("=",end="")
    print(item_c,end="")
elif((item_a / item_b) ==item_c):
    print(item_a,end="")
    print("/",end="")
    print(item_b,end="")
    print("=",end="")30
    print(item_c,end="")
else:
    print(item_a,end="")
    print("*",end="")
    print(item_b,end="")
    print("=",end="")
    print(item_c,end="")