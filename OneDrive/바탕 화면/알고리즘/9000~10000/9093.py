for _ in range(int(input())):
    items = input().split()
    line = []
    for j in range(len(items)):
        line.append("".join(list(reversed(items[j]))))
    print(" ".join(line))
        