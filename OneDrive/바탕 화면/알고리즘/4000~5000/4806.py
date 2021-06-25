ctr = 0
while(True):
    try:
        item = input()
        ctr +=1
    except EOFError:
        break
print(ctr)