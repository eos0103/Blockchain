items_stack = []
for i in range(int(input())):
    items = input().split()
    if(items[0] == "push"):
        items_stack.append(items[1])
    if(items[0] == "pop"):
        try:
            print(items_stack.pop())
        except:
            print(-1)
    if(items[0] == "size"):
        print(len(items_stack))
    if(items[0] == "empty"):
        if(len(items_stack) == 0):
            print(1)
        else:
            print(0)
    else:
        if(len(items_stack) != 0):
            print(items_stack[len(items_stack)-1])
        else:
            print("-1")