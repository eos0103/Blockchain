sum = ""
for i in range(2):
    item = input()
    if(item =='black'):
        sum+="0"
    elif(item =='brown'):
        sum+="1"
    elif(item =='red'):
        sum+="2"
    elif(item =='orange'):
        sum+="3"
    elif(item =='yellow'):
        sum+="4"
    elif(item =='green'):
        sum+="5"
    elif(item =='blue'):
        sum+="6"
    elif(item =='violet'):
        sum+="7"
    elif(item =='grey'):
        sum+="8"
    elif(item =='white'):
        sum+="9"
sum = int(sum)
item = input()
if(item =='black'):
    sum*=1
elif(item =='brown'):
    sum*=10
elif(item =='red'):
    sum*=100
elif(item =='orange'):
    sum*=1000
elif(item =='yellow'):
    sum*=10000
elif(item =='green'):
    sum*=100000
elif(item =='blue'):
    sum*=1000000
elif(item =='violet'):
    sum*=10000000
elif(item =='grey'):
    sum*=100000000
elif(item =='white'):
    sum*=1000000000
print(sum)