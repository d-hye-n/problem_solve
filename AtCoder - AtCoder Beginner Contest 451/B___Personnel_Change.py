n, m = map(int, input().split())
now = [0 for _ in range(n)]
next = [0 for _ in range(n)]

for _ in range(n):
    a, b = map(int, input().split())
    now[a-1] += 1
    next[b-1] += 1

for i in range(m):
    print(next[i]-now[i])