n = int(input())
ans = []
for i in range(1,n+1):
    ans.append(i)
print(*list(reversed(ans)), sep=",")