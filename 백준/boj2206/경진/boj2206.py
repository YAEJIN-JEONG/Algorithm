# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

arr = [stdin.readline().rstrip() for _ in range(n)]

deq = deque()
# (x, y, 벽 부수기 가능 횟수)
deq.append((0, 0, 1))
# visited[x][y][0] = (x, y) 위치 벽 부수고 도착
# visited[x][y][1] = (x, y) 위치 벽 안 부수고 도착
visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]
visited[0][0] = [0, 0]

while deq:
    x, y, crush = deq.popleft()

    # 최종 위치 도달. 시작과 끝 칸을 포함하므로 구한 거리 + 1 출력
    if x == n - 1 and y == m - 1:
        print(visited[x][y][crush] + 1)
        break

    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]

        if 0 <= nx < n and 0 <= ny < m:
            # 지나갈 수 있는 곳이고, 아직 방문 x
            if arr[nx][ny] == '0' and visited[nx][ny][crush] == -1:
                deq.append((nx, ny, crush))
                visited[nx][ny][crush] = visited[x][y][crush] + 1
            # 못가는 곳인데 벽 부수기 횟수 있고, 아직 방문 x
            elif arr[nx][ny] == '1' and crush > 0 and visited[nx][ny][crush - 1] == -1:
                deq.append((nx, ny, crush - 1))
                visited[nx][ny][crush - 1] = visited[x][y][crush] + 1
# 경로가 없는 경우
else:
    print(-1)
