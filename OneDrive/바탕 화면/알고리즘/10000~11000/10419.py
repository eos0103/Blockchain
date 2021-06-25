for i in range(int(input())):
    item = int(input())
    ctr = 1
    while(True):
        if(ctr + ctr**2 <= item):
            ctr+=1
        else:
            print(ctr-1)
            break
    