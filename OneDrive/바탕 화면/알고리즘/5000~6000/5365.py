for _ in range(int(input())):
    items = input().split()
    line = items[:2]
    print(" ".join(items[2:])," ".join(line))