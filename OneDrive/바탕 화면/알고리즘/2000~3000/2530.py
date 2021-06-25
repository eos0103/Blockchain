item_a, item_b, item_c = map(int, input().split())
took_time = int(input()) 
remainder = took_time % 60
minute_add = took_time%3600//60 
ctr_hour = 0
ctr_minute = 0

if(item_c+remainder>=60):
    item_c = (item_c + remainder)-60
    ctr_minute += 1
else:
    item_c = item_c + remainder

minute_add += ctr_minute
if(item_b + minute_add >= 60):
    item_b = (item_b + minute_add)-60
    ctr_hour += 1
else:
    item_b += minute_add 

hour_add = took_time//3600
hour_add += ctr_hour 

item_a = (item_a + hour_add)%24

print(item_a,item_b,item_c)

