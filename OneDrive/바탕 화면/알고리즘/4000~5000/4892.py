items = []
while(True):
    ctr = 0
    item = int(input())
    if(item == 0):
        break
    items.append(item)

for i in range(len(items)):
    print(i+1, end="")
    result_1 = items[i]*3
    if(result_1 %2 != 0):
        result_2 = (result_1+1)/2
        result_3 = result_2*3
        result_4 = result_3//9
        print(". odd", int(result_4))
    else:
        result_2 = result_1/2
        result_3 = result_2*3
        result_4 = result_3//9
        print(". even", int(result_4))
    result_1 = 0
    result_2 = 0
    result_3 = 0
    result_4 = 0