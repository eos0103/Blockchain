for _ in range(int(input())):
    item = input()
    rev_item = int("".join(list(reversed(item))))
    item_a = int(item)+rev_item
    item_b = int("".join(list(reversed(str(item_a)))))
    if(item_a == item_b):
        print("YES")
    else:
        print("NO")