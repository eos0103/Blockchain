grade_a = 0
grade_b = 0
for _ in range(int(input())):
    item_a, item_b = map(int, input().split())
    if(item_a > item_b):
        grade_a += 1
    elif(item_a < item_b):
        grade_b += 1
print(grade_a, grade_b)
    