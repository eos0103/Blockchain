listen_ctn, see_ctn = map(int, input().split())
listen_items = []
see_items = []
for i in range(listen_ctn):
    listen_items.append(input())
for i in range(see_ctn):
    see_items.append(input())
what_items = []
if(listen_ctn >= see_ctn):
    for i in range(len(see_items)):
        if(see_items[i] in listen_items):
            what_items.append(see_items[i])
else:
    for i in range(len(listen_items)):
        if(listen_items[i] in see_items):
            what_items.append(listen_items[i])
print(sorted(what_items))