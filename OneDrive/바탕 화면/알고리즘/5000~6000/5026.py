for _ in range(int(input())):
    item = input().split("+")
    if(len(item)== 1):
        print("skipped")
    else:
        print(int(item[0])+int(item[1]))