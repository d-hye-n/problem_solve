a = int(input()) ## 테스트 케이스 수
for _ in range(a):
    m, n, k = map(int, input().split()) ## 가로, 세로, 배추 개수
    graph = [[0] * m for _ in range(n)] ## 배추밭 초기화
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1 ## 배추 위치 표시

    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 0 ## 방문 처리
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return True
        return False

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(j, i):
                count += 1 ## 새로운 배추군집 발견 시 카운트 증가

    print(count) ## 결과 출력