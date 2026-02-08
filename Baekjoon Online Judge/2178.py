import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]

queue = deque([(0,0)])
dist[0][0] = 1
dy = [-1,1,0,0]
dx = [0,0,-1,1]
while queue:
    y, x = queue.popleft()
    if y == n-1 and x == m-1:
        print(dist[y][x])
        break
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if grid[ny][nx] == 1 and dist[ny][nx] == 0:
                dist[ny][nx] = dist[y][x]+1
                queue.append((ny,nx))