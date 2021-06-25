items = list(input())
happy_cnt = 0
sad_cnt = 0
for i in range(len(items)):
    if(items[i] == ":"):
        try:
            if(items[i+2]=="("):
                sad_cnt += 1
            else:
                happy_cnt += 1
        except:
            pass
if(happy_cnt == 0 and sad_cnt == 0):
    print("none")
else:
    if(happy_cnt > sad_cnt):
        print("happy")
    elif(happy_cnt < sad_cnt):
        print("sad")
    else:
        print("unsure")