while(True):
    item = list(input())
    if(item[0] == "#"):
        break
    else:
        while(True):
            if(item[0] == "A" or item[0] == "E" or item[0] == "I" or item[0] == "O" or item[0] == "U" or item[0] == "a" or item[0] == "e" or item[0] == "i" or item[0] == "o" or item[0] == "u"):
                print("".join(item)+"ay")
                break
            else:
                temp = item[0]
                del item[0]
                item.append(temp)