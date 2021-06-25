def roundTraditional(val,digits):
   return round(val+10**(-len(str(val))-1), digits)
for _ in range(int(input())):
    item = roundTraditional((float(input())/5)*4,2)
    print("$%.2f" %item)
