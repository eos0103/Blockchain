item_a, item_b = map(int, input().split())
took = int(input())
remainder = took % 60
item_a_plus = took // 60

if (item_b + remainder >=60):
    item_b = (item_b + remainder)-60
    item_a_plus+=1
else:
    item_b = item_b + remainder 

item_a = item_a + item_a_plus

if(item_a >= 24):
    print(item_a%24, item_b)
else:
    print(item_a, item_b)
