items = input().split()
items_a = list(items[0])
items_b = list(items[1])

for i in range(len(items_a)):
    if(items_a[i]=="5"):
        item_a[i] = "6"
for i in range(len(items_a)):
    if(items_b[i]=="5"):
        item_b[i] = "6"
print(int("".join(list(map(str, items_a)))) + int("".join(list(map(str, items_b)))))

# items_a = list(items[0])
# items_b = list(items[1])
# print(items_a)
# print(items_b)
# for i in range(len(items_a)):
#     if(items_a[i]==5)