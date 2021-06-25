for _ in range(int(input())):
    count, _ = map(int, input().split())
    line = []
    for _ in range(count):
        line.append(int(input()))
    print(count-len(list(set(line))))