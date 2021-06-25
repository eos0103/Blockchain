item = int(input())
cnt = 2
inc = 6
sum = 2
if(item == 1):
    print("1")
else:
    while(True):
        if(sum + inc > item ):
            print(cnt)
            break
        else:
            cnt += 1
            sum += inc
            inc += 6
            # print(sum)