import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
count = 0
for _ in range(n):
    a = list(map(int, input().split()))
    sum = 0
    for i in range(m):
        sum += b[i]*a[i]
    if sum + c > 0:
        count += 1

print(count)