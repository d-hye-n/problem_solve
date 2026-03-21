n = int(input())
C = [[0] * n for _ in range(n)]
for i in range(n - 1):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        C[i][i + j + 1] = row[j]

for a in range(n-2):
    for b in range(a, n-1):
        for c in range(b, n):
            if C[a][c] > C[a][b] + C[b][c]:
                print('Yes')
                exit()

print("No")