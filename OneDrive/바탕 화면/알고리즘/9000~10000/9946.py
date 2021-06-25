j = 1
while(True):
    items_a = input()
    items_b = input()
    if(items_a =="END"):
        break
    else:
        len_a = len(items_a)
        items_a = list(set(list(items_a)))
        items_b = list(items_b)
        len_b = 0
        for i in range(len(items_a)):
            len_b += items_b.count(items_a[i])
        if(len_a == len_b):
            print("Case",j,end="")
            print(": same")
        else:
            print("Case",j,end="")
            print(": different")
        j+=1