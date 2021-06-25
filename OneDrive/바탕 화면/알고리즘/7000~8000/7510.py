ctn = int(input())
for i in range(ctn):
    items = list(map(int, input().split()))
    min_a = min(items)
    items.remove(min_a)
    max_a = max(items)
    items.remove(max(items))
    rem = items[0]
    if((rem**2)+(min_a**2) == max_a**2):
        print("Scenario #",end="")
        print(i+1,end=":")
        print()
        print("yes")
    else:
        print("Scenario #",end="")
        print(i+1,end=":")
        print()
        print("no")
    if(i == ctn-1):
        pass
    else:
        print()