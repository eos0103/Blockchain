for _ in range(int(input())):
    ctn, con = map(int ,input().split())
    items = list(map(int , input().split()))
    sum = 0
    for i in range(ctn):
        sum += items[i]//con
    print(sum)