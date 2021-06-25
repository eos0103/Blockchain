sum = 0
for i in range(int(input())):
    item_a, item_b = input().split("-")
    for i in range(len(item_a)):
        sum = sum + ord(item_a[i])*(26**(2-i))
        print(sum)
    print(sum)
    sum = 0
