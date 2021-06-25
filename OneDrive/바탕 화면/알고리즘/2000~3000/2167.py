col, row = map(int, input().split())
items = []
for i in range(col):
    items.append(list(map(int, input().split())))
# print(items)
for i in range(int(input())):
    min_a, max_a, min_b, max_b = map(int, input().split())
    sum = 0
    for j in range(row):
        for k in range(col):
            if(min_a-1<=k and k <= min_b-1 and max_a-1 <= j and j <= max_b-1):
                sum += items[k][j]
                # print("min_a = ",min_a,"max_a = ",max_a,"min_b = ",min_b,"max_b = ",max_b)
                # print(sum)
    print(sum)
