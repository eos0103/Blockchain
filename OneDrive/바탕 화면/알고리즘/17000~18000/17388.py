items = list(map(int, input().split()))

value = min(items)

if(sum(items) >= 100):
    print("OK")
else:
    if(value == items[0]):
        print("Soongsil")
    elif(value == items[1]):
        print("Korea")
    else:
        print("Hanyang")