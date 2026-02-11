import math
a, b = map(str,input().split())
c = int(a+b)
if int(c**0.5)**2 == c:
    print("Yes")
else:
    print("No")
