items = [0] * 5
for _ in range(int(input())):
    item_a, item_b = map(int, input().split())
    if(item_a == 0 or item_b == 0):
        items[4]+=1
    else:
        if(item_a > 0 and item_b >0):
            items[0]+=1
        elif(item_a > 0 and item_b < 0):
            items[3]+=1
        elif(item_a < 0 and item_b > 0):
            items[1]+=1
        else:
            items[2]+=1
print("Q1:", items[0])
print("Q2:", items[1])
print("Q3:", items[2])
print("Q4:", items4[3])
print("AXIS:", items[4])
            
        