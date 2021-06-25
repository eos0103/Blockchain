input()
items = list(input())
ctr_e = items.count("e")
ctr_a = items.count("2")
if(ctr_a > ctr_e):
    print("2")
elif(ctr_a == ctr_e):
    print("yee")
else:
    print("e")