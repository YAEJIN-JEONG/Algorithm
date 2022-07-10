from collections import deque
# 너비 우선 탐색
def bfs(graph,x, y):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽이 아니므로 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

t = int(input())

for i in range(t):
    cnt = 0
    n,m,k = map(int, input().split())
    graph = [[0 for i in range(m)]
                    for j in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)