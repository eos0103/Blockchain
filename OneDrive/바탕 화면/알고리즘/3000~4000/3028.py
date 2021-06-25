items = list(input())
line = [1, 2, 3]
for i in range(len(items)):
    if(items[i] == "A"):
        temp = line[0]
        line[0] = line[1]
        line[1] = temp
    elif(items[i] == "B"):
        temp = line[1]
        line[1] = line[2]
        line[2] = temp
    else:
        temp = line[0]
        line[0] = line[2]
        line[2] = temp
print(line.index(1)+1)
