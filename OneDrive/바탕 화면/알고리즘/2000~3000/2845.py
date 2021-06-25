item_a, item_b = map(int, input().split())
items = list(map(int, input().split()))
for i in range(len(items)):
    print(items[i]-(item_a*item_b),end=" ")