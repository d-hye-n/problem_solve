import math

h, w = map(int,input().split())
if h == 1 or w == 1:
    print(1)
else:
    print(int(math.ceil(h*w/2)))