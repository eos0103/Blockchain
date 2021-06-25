for _ in range(int(input())):
    items = list(input())
    ctr_a = 0
    ctr_b = 0
    for i in range(len(items)):
        if(items[i] == ')'):
            ctr_a +=1
        else:
            ctr_b +=1
    if(ctr_a == ctr_b):
        print("YES")
    else:
        print("NO")