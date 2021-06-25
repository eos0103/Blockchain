items = list(input())
sum = 10
for i in range(1, len(items)):
    if( items[i] == items[i-1]):
        sum += 5
    else:
        sum += 10
print(sum)