for _ in range(int(input())):
    items = list(input())
    count = int(input())
    line = input()
    sign = 0
    for i in range(len(items)):
        if(items[i] == "R"):
            line = list(reversed(line))
        elif(items[i] == "R"):
            try:
                del line[0]
            except:
                print("error")
                sign +=1
                break
    if(sign != 1):
        print()
    