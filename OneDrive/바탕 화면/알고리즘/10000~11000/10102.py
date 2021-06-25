input()
items = list(input())
items_a = items.count("A")
items_b = items.count("B")
if(items_a > items_b):
    print("A")
elif(items_a < items_b):
    print("B")
else:
    print("Tie")