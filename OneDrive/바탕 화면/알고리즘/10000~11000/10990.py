count = int(input())
for k in range(count):
    for j in range(k):
        print(" ", end="")
    for i in range(count):
        print("*", end="")
    print()