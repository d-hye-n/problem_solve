import sys
x = int(sys.stdin.readline())
ans = ":("

for n in range(1, x + 1):
    if int(n * 1.08) == x:
        ans = n
        break

print(ans)