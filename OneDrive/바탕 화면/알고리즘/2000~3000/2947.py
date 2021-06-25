items = list(map(int, input().split()))

i = 0
max = -1323123

while(items != [1, 2, 3, 4, 5]):
    for i in range(len(items)-1):
        if(items[i] > items[i+1]):
            temp = items[i]
            items[i] = items[i+1]
            items[i+1] = temp
            print(" ".join(list(map(str, items))))
   