count = int(input())

for j in range(1, count+1):
    for i in range(j):
        print("*",end="")
    for k in range(count-j):
        print(" ",end="")
    for k in range(count-j):
        print(" ",end="")   
    for i in range(j):
        print("*",end="")
    print()
for j in range(1, count+1):
    for i in range(count-j):
        print("*",end="")
    for k in range(j):
        print(" ",end="")
    for k in range(j):
        print(" ",end="")       
    for i in range(count-j):
        print("*",end="")
    print()
    