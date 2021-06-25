items = list(map(int, input().split()))
items_alpha = list(input())
items_dict = {}
for i in range(3):
    items_dict[items_alpha[i]] = items[i] 
print(items_dict)
    