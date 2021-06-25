row, col = map(int, input().split())
row_cnt, col_cnt = map(int, input().split())
cnt = 0
for j in range(row):
    for i in range(col):
        if(cnt % 2 == 0):
            for k in range(row_cnt):
                for h in range(col_cnt):
                    print("X")
                print()
        else:


    cnt+=1 