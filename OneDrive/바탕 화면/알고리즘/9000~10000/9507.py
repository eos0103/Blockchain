def fib(ctn):
    if(ctn < 2):
        return 1
    elif(ctn == 2):
        return 2
    elif(ctn == 3):
        return 4
    else:
        return fib(ctn-1) + fib(ctn-2) + fib(ctn-3) +  fib(ctn-4)
print(fib(int(input())))