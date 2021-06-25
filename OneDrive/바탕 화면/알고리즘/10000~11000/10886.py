items = []
for i in range(int(input())):
    items.append(int(input()))
count_zero = items.count(0)
count_one = items.count(1)
if( count_zero >= count_one ):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")