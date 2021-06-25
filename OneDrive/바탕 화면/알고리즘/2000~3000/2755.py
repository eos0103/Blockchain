import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

items_grade = {
    "A+": 4.3,
    "A0": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B0": 3.0,
    "B-": 2.7,
    "C+": 2.3,  
    "C0": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D0": 1.0,
    "D-": 0.7,
    "F": 0.0,
    }
sum = 0
div_sum = 0
for i in range(int(input())):
    items = input().split()
    sum += int(items[1]) * items_grade[items[2]]
    div_sum += int(items[1])
a = round_half_up(sum/div_sum, 2) 
print("%.02f" %(a))