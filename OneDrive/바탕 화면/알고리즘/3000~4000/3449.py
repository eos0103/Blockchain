for _ in range(int(input())):
    items_a = list(input())
    items_b = list(input())
    cnt = 0
    for i in range(len(items_a)):
        if(items_a[i] != items_b[i]):
            cnt +=1
    print("Hamming distance is",cnt,end=".\n")