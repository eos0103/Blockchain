col, row = map(int, input().split()) 
board = []
ctr = 0
value = 0
for i in range(col):
    board.append(list(input()))
for j in range(col):
    for i in range(row):
        if(board[j][i] == "X"):
            ctr +=1
            # print(j)
    if(ctr >= 1):
        value += 1
        ctr = 0
print(col-value)