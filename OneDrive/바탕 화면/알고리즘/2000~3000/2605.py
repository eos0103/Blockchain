count = int(input())
line = []
items = list(map(int, input().split()))
if(count == 0):
    print("1 2 3 4")
else:
    for i in range(count):
        line.insert(items[i]-i, i+1)
    print(" ".join(list(map(str, line))))