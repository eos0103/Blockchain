dou_ctn = int(input())
for _ in range(dou_ctn):
    price = int(input())
    opt = int(input())
    sum = 0
    if(price == 0):
        print(opt)
    else:
        for _ in range(opt):
           item_a, item_b = map(int, input().split())
           sum += item_a * item_b
        print(price + sum) 