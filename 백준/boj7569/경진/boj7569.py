# https://www.acmicpc.net/problem/7569
# 토마토
from sys import stdin
from collections import deque

# m: 열, n: 행, h: 높이
m, n, h = map(int, stdin.readline().split())

box = [[[i for i in stdin.readline().split()] for _ in range(n)] for _ in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

deq = deque()
# 초기 큐 세팅 (익은 토마토 위치를 큐에 입력)
for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == '1':
                deq.append((z, x, y))
# bfs
while deq:
    z, x, y = deq.popleft()

    steps = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    # 익은 토마토 주변 토마토 익히기, visited 에 카운트 저장
    for step in steps:
        nz = z + step[0]
        nx = x + step[1]
        ny = y + step[2]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and visited[nz][nx][ny] == 0 and box[nz][nx][ny] == '0':
            deq.append((nz, nx, ny))
            box[nz][nx][ny] = '1'
            visited[nz][nx][ny] = visited[z][x][y] + 1

answer = 0
# 가장 높은 카운트 answer 에 저장, 안 익은 토마토 있으면 answer = -1, 반복문 종료 (예외 발생)
try:
    for z in range(h):
        for x in range(n):
            for y in range(m):
                answer = max(answer, visited[z][x][y])
                if box[z][x][y] == '0':
                    answer = -1
                    raise Exception()
except Exception:
    pass
# 정답 출력
print(answer)
