items = list(input())
set_items = list(set(items))
# print(set_items)
items_ctr = []
sign = 0
for i in range(len(set_items)):
    items_ctr.append(items.count(set_items[i]))
count_sign = items_ctr[0]
for i in range(len(items_ctr)):
    if(items_ctr[i] % count_sign != 0):
        # print("I\'m Sorry Hansoo")
        sign += 1
        break  
set_items.sort()
if(sign == 1):
    print("I\'m Sorry Hansoo")
else:
    print(sorted(items))