for i in range(int(input())):
    items = list(map(int, input().split()))
    sum = 0
    min = 123424
    for i in range(len(items)):
        if(items[i] % 2 == 0):
           sum += items[i]
           if(min > items[i]):
               min = items[i]
    print(sum, min)