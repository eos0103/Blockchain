item_a, item_b = map(int, input().split())
item_c, item_d = map(int, input().split())
if(item_c + item_b > item_a + item_d):
    print(item_a + item_d)
else:
    print(item_c + item_b)    