def fibonacci(count):
    if(count == 1):
        return 1
    if(count == 2 ):
        return 2
    else:
        return fibonacci(count-1) + fibonacci(count-2) 

item = int(input())-1
print(fibonacci(item))
