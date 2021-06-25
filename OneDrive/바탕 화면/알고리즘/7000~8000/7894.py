for _ in range(int(input())):
    ctn = int(input())
    sum = 1
    for i in range(1, ctn+1):
        sum *= i
    print(len(str(sum)))