items = []
for _ in range(3):
    items.append(int(input()))
if(sum(items)==180):
    if(items[0]==60 & items[1]==60 & items[2]==60):
        print("Equilateral")
    else:
        if(items[0]==items[1] or items[1]==items[2] or items[0]==items[2]):
            print("Isosceles")
        else:
            print("Scalene")
else:
    print("Error")