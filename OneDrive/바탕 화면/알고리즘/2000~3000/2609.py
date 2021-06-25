count = int(input())
def gcd(a, b):
	while(b!=0):
		r = a%b
		a= b
		b= r
	return a
for _ in range(count):
    a,b = map(int,input().split())
    c = gcd(a,b)
    print(int(a*b/c))