# https://www.acmicpc.net/problem/2178
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

array = []
for _ in range(n):
    array.append(list(stdin.readline()))

# bfs
dq = deque()
dq.append((0, 0))
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1

while dq:
    x, y = dq.popleft()

    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for step in steps:
        nx = x + step[0]
        ny = y + step[1]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and array[nx][ny] == '1':
            dq.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

print(visited[n - 1][m - 1])
