while(True):
    items = input()
    if(items == "END"):
        break
    else:
        print("".join(list(reversed(list(items)))))