a, b, c, d = map(int, input().split())
 
vertical_min = c-a
horizontal_min = d-b
if(vertical_min > a):
    vertical_value = a
else:
    vertical_value = vertical_min
if(horizontal_min > b):
    horizontal_value = b
else:
    horizontal_value = horizontal_min
if(vertical_value > horizontal_value):
    print(horizontal_value)
else:
    print(vertical_value)
