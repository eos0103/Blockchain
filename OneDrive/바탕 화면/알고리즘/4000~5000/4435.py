for j in range(int(input())):
    items_a = list(map(int, input().split()))
    items_b = list(map(int, input().split()))
    sum_a = 0
    sum_b = 0
    sum_a += items_a[0] * 1
    sum_a += items_a[1] * 2
    sum_a += items_a[2] * 3
    sum_a += items_a[3] * 3 
    sum_a += items_a[4] * 4 
    sum_a += items_a[5] * 10

    sum_b += items_b[0] * 1
    sum_b += items_b[1] * 2
    sum_b += items_b[2] * 2
    sum_b += items_b[3] * 2 
    sum_b += items_b[4] * 3 
    sum_b += items_b[5] * 5
    sum_b += items_b[6] * 10

    if (sum_a > sum_b):
        print("Battle",j+1,end="")
        print(": Good triumphs over Evil")
    elif (sum_a < sum_b):
        print("Battle",j+1,end="")
        print(": Evil eradicates all trace of Good")
    else:
        print("Battle",j+1,end="")
        print(": No victor on this battle field")