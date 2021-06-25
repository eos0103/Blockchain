index_items = []
for j in range(5):
    items = list(input())
    for i in range(len(items)):
        if(items[i]=="F"):
            try:
                if(items[i+1]=="B" and items[i+2] == "I"):
                    index_items.append(j+1)
            except:
                pass
for i in range(len(index_items)):
    print(index_items[i],end=" ") 
