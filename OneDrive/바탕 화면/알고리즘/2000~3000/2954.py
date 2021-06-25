items = list(input())
i = 0
while(i <= len(items)):
    try:
        if(items[i]=="a" or items[i]=="e" or items[i]=="i" or items[i]=="o" or items[i]=="u"):
            print(items[i], end="")
            i+=2
        else:
            print(items[i], end="")
    except:
        pass
    i += 1 
