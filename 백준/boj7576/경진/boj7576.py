# https://www.acmicpc.net/problem/7576
# 토마토
from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
box = [[i for i in stdin.readline().split()] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

deq = deque()
# 초기 셋팅 (익은 토마토 위치를 큐에 넣기)
for x in range(n):
    for y in range(m):
        if box[x][y] == '1':
            deq.append((x, y))
# bfs
while deq:
    x, y = deq.popleft()

    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 익은 토마토 주변 토마토 익히기, visited 에 카운트 저장
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and box[nx][ny] == '0':
            box[nx][ny] = '1'
            visited[nx][ny] = visited[x][y] + 1
            deq.append((nx, ny))

answer = 0
# 가장 높은 카운트 answer 에 저장, 안 익은 토마토 있으면 answer = -1, 반복문 종료
for x in range(n):
    for y in range(m):
        answer = max(answer, visited[x][y])
        if box[x][y] == '0':
            answer = -1
            break
    else:
        continue
    break

print(answer)
