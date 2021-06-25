for _ in range(int(input())):
    items = list(map(int, input().split()))
    items.remove(max(items)) 
    items.remove(min(items))
    if(max(items)-min(items)>=4):
        print("KIN")
    else:
        print(sum(items))