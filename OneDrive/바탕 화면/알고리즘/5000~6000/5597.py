a = [0] * 30
# print(a)
for _ in range(28):
    a[int(input())-1] = 1
# print(a)
for i in range(30):
    if(a[i]) == 0:
        print(i+1)