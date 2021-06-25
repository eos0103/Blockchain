count = int(input())
items = list(map(int, input().split()))
board = [0]*100
ctr = 0
for i in range(count):
    if(board[items[i]+1]==0):
        board[items[i]+1] = 1
    else:
        ctr += 1
print(ctr)