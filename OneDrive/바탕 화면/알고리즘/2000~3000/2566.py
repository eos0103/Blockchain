# board = [[0]*10]*10
max = 0
items = []
for _ in range(9):
    items.append(list(map(int,input().split())))
for j in range(9):
    for i in range(9):
        if(items[j][i] > max):
            max = items[j][i]
            xposition = i
            yposition = j
print(max)
print(yposition+1, xposition+1)