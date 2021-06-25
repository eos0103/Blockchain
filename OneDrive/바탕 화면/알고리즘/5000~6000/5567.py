items_a = []
items_b = [] 
for i in range(10):
    items_a.append(int(input()))
for i in range(10):
    items_b.append(int(input()))
items_a.sort()
items_b.sort()
print(sum(items_a[7:10]),end=" ")
print(sum(items_b[7:10]))