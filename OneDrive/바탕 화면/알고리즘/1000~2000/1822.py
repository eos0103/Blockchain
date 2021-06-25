a_cnt, b_cnt = map(int, input().split())
a_items = list(map(int, input().split()))
b_items = list(map(int, input().split()))
cnt = 0
for i in range(b_cnt):
    try:
        a_items.remove(b_items[i])
        cnt += 1
    except:
        pass
if(len(a_items)==0):
    print("0")
else:
    print(len(a_items))
    print(" ".join(list(map(str,a_items))))