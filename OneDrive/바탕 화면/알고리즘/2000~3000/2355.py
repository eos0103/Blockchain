import math
min_b, max_a = map(int, input().split())
if(min_b == max_a):
    print(min_b*2)
else:
    if min_b > max_a:
        temp = min_b
        min_b = max_a
        max_a = temp
    min_b = min_b -1
    print(int((max_a*(max_a+1))/2)-int((min_b*(min_b+1))/2))