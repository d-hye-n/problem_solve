h, w, q = map(int, input().split())
for i in range(q):
    q, c = map(int, input().split())
    if q == 1:
        eat = w*c
        h -= c
    elif q == 2:
        eat = h*c
        w -= c

    print(eat)