sum = 0
max_count = 0
for _ in range(int(input())):
    item_a, item_b = map(int, input().split())
    if(item_a > item_b):
        max_count += item_b
    else:
        for i in range(1, 101):
            if(item_b < item_a * i):
                break
            else:
                max_count = item_b - (item_a * (i))
    sum += max_count
    # print(sum)
    max_count = 0
print(sum)