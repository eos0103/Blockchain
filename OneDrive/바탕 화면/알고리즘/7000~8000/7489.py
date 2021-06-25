for _ in range(int(input())):
    item = int(input())
    sum = 1
    for i in range(2, item+1):
        sum *= i
    line = str(sum)
    # print(line)
    for j in range(len(line)-1, -1, -1):
        if(line[j] == "0"):
            pass
        else:
            print(line[j])
            break