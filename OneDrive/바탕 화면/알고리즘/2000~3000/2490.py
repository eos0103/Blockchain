for i in range(3):
    a = list(map(int, input().split()))
    sum = a.count(0)
    if(sum == 0):
        print("E")
    elif(sum == 1):
        print("A")
    elif(sum == 2):
        print("B")
    elif(sum == 3):
        print("C")
    elif(sum == 4):
        print("D")    

