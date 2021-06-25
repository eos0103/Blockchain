value = 0
max = 0
for _ in range(int(input())):
    one, two, three = map(int, input().split())
    if(one == two == three):
        value = 10000+one*1000
    else:
        if(one == two or one == three or two == three):
            if(one == two):
                value = 1000 + one*100
            elif(one == three):
                value = 1000 + one * 100
            else:
                value = 1000 + two * 100
        else:
            max_this = one
            if(max_this < two):
                max_this = two
            if(max_this < three):
                max_this = three
            value = 100 * max_this
    if(value > max):
        max = value
print(max)