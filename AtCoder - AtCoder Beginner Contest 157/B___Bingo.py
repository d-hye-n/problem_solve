grid = [list(map(int, input().split())) for _ in range(3)]
marked = [[False] * 3 for _ in range(3)]
N = int(input())

for _ in range(N):
    temp = int(input())
    for j in range(3):
        for k in range(3):
            if grid[j][k] == temp:
                marked[j][k] = True

for i in range(3):
    if marked[i][0] and marked[i][1] and marked[i][2]:
        print("Yes")
        exit()

for i in range(3):
    if marked[0][i] and marked[1][i] and marked[2][i]:
        print("Yes")
        exit()

if marked[0][0] and marked[1][1] and marked[2][2]:
    print("Yes")
    exit()
if marked[0][2] and marked[1][1] and marked[2][0]:
    print("Yes")
    exit()

print("No")