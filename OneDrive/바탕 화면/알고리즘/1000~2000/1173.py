time, min_rate, max_rate, plus, minus = map(int, input().split())
now_rate = min_rate
ctr = 0
while(time > 0):
    if(now_rate + plus <= max_rate):
        now_rate += plus
        time -= 1
        ctr +=1
    else:
        if(now_rate-minus < min_rate and now_rate + plus > max_rate):
            ctr = -1
            break
        else:
            now_rate -= minus 
            ctr +=1
if(ctr == "-1"):
    print("-1")
else:
    print(ctr)