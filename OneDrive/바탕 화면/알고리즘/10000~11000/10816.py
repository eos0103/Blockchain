import sys
sys.stdin=open("input.txt","r")

c = []
input()
a = input().split()
count = int(input())
b = input().split()
for i in range(count):
    c.append(a.count(b[i]))
print(" ".join(list(map(str,c))))