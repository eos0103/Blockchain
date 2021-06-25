row, col, number = map(int, input().split())
board = [[0] * row]*col
ctr = -1
for j in range(row):
    for i in range(col):
        ctr +=1
        if(ctr == number):
            x_position = i
            y_position = j
            break
    if(ctr == number):
            break
            
print(y_position, x_position)