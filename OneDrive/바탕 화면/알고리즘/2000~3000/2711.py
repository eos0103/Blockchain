for i in range(int(input())):
    ind, item = input().split()
    item = list(item)
    del(item[int(ind)-1]) 
    print("".join(item))
