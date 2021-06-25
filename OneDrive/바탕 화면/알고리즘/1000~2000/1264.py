sum = 0
while(True):
    items = input().split()
    for i in range(len(items)):
        sum += items[i].count("a")
        sum += items[i].count("e")
        sum += items[i].count("i")
        sum += items[i].count("o")
        sum += items[i].count("u")
        sum += items[i].count("A")
        sum += items[i].count("E")
        sum += items[i].count("I")
        sum += items[i].count("O")
        sum += items[i].count("U")
    if(items[0] == "#"):
        break
    print(sum)
    sum = 0 