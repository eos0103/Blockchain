for i in range(int(input())):
    item_a, item_b, item_c = map(int, input().split())
    line = []
    line.append(item_a)
    line.append(item_b)
    line.append(item_c)
    line_a = max(line)
    line.remove(line_a)
    line_b = min(line)
    line.remove(line_b)
    
    if(line[0]+(line_b) < line_a):
        print("Case #",end="")
        print(i+1, end="")
        print(": invalid!")
    else:
        if(item_a == item_b == item_c):
            print("Case #",end="")
            print(i+1, end="")
            print(": equilateral")
        else:
            if(item_a == item_b or item_b == item_c or item_c == item_a):
                print("Case #",end="")
                print(i+1, end="")
                print(": isosceles")
            else:
                print("Case #",end="")
                print(i+1, end="")
                print(": scalene")
