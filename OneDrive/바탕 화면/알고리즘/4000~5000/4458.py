values = []
pri_values = []
for _ in range(int(input())):
    items = input().split()
    for i in range(len(items)):
        sep_item = list(items[i])
        sep_item[0] = sep_item[0].upper()
        values.append("".join(sep_item))
    pri_values.append(" ".join(values))
    # for i in range(len(values)):
    #     pri_values.append(values[i])
    values.clear()
for i in range(len(pri_values)):
    print(pri_values[i])
