items = list(map(int, input().split()))
if(items[0]==items[1] and items[0]==items[2] and items[1]==items[2]):
    print(10000+items[0]*1000)
else:
    if(items[0]==items[1] or items[0]==items[2] or items[1]==items[2]):
        if(items.count(items[0])==2):
            print(1000+items[0]*100)
        else:
            print(1000+items[1]*100)
    else:
        print(max(items)*100)