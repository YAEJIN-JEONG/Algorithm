# https://programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    deq = deque([(0, 0)])
    visited[0][0] = 1

    # bfs
    while deq:
        x, y = deq.popleft()

        if (x, y) == (n - 1, m - 1):
            break

        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                deq.append((nx, ny))
    else:
        return -1

    return visited[n - 1][m - 1]
