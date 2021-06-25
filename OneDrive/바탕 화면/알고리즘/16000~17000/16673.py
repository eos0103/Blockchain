count, mul_cnt, buy_cnt = map(int, input().split())
sum = 0
for i in range(1, count+1):
    sum+= mul_cnt*i + buy_cnt*(i*i)
print(sum)