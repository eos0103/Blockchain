items_dict = {}
for _ in range(int(input())):
    for _ in range(int(input())):
        items = input().split()
        try:
            items_dict[items[0]] += int(items[1])
        except:
            items_dict[items[0]] = int(items[1])
    print(max(items_dict, key=items_dict.get))
    items_dict = {}