items_a = list(map(int, input().split()))
items_b = list(map(int, input().split()))
if(sum(items_a) > sum(items_b) ):
    winner_items = items_a
    lose_items = items_b
else:
    winner_items = items_b
    lose_items = items_a
   
grade_winner = 0
grade_lose = 0
reversal = 0
win_sign = 0
for i in range(len(items_a)):
    grade_winner += winner_items[i]
    grade_lose += lose_items[i]
    if(grade_winner < grade_lose):
        win_sign = 1
    if(win_sign == 1 and grade_winner > grade_lose):
        reversal = 1
if(reversal != 0):
    print("Yes")
else:
    print("No")