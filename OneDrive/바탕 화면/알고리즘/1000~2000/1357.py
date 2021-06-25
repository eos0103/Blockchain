a, b = map(list, input().split())
a = int("".join(reversed(a)))
b = int("".join(reversed(b)))
print(int("".join(reversed(str(a + b))))) 
