for _ in range(int(input())):
    sum_a = 0
    sum_b = 0
    for _ in range(9):
        item_a, item_b = map(int, input().split())
        sum_a += item_a
        sum_b += item_b
    if(sum_a > sum_b):
        print("Yonsei")
    elif(sum_a < sum_b):
        print("Korea")
    else:
        print("Draw")