# https://www.acmicpc.net/problem/2573
# 빙산
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

target = set()
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if arr[i][j] > 0:
            target.add((i, j))

xyd = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 1년 지날 때 마다
def process():
    global target, xyd
    erase = set()
    for t in target:
        cnt = 0
        for d in xyd:
            nx, ny = t[0] + d[0], t[1] + d[1]
            if (nx, ny) not in target:
                cnt += 1
        arr[t[0]][t[1]] = max(0, arr[t[0]][t[1]] - cnt)
        if arr[t[0]][t[1]] == 0:
            erase.add((t[0], t[1]))

    target -= erase


# 영역 탐색
def navigate(start_x, start_y):
    global n, m, xyd
    stack = [[start_x, start_y]]
    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = True
    area = 0
    while stack:
        x, y = stack.pop()
        area += 1

        for d in xyd:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != 0:
                stack.append([nx, ny])
                visited[nx][ny] = True

    return area


# 진행
year = 0
while target:
    i, j = target.pop()
    target.add((i, j))
    if navigate(i, j) < len(target):
        break
    process()
    year += 1

print(year if target else 0)
