for _ in range(int(input())):
    input()
    items = list(map(int, input().split()))
    print((max(items)-min(items))*2)