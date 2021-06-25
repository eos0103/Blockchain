item, count, value = map(int, input().split())
if (item*count >= value):
    print(item*count - value)
else:
    print("0")