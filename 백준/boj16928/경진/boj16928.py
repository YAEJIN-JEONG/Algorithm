# https://www.acmicpc.net/problem/16928
# 뱀과 사다리 게임
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

# 사다리, 뱀 -> {시작: 끝}
ladder_snake = {}
for _ in range(n + m):
    u, v = map(int, stdin.readline().split())
    ladder_snake[u] = v

# bfs
deq = deque()
# 큐에 튜플 입력 (현재 위치, 주사위 던진 횟수)
deq.append((1, 0))
visited = [False] * 101
visited[1] = True

while deq:
    x, cnt = deq.popleft()

    # 끝 지점 도착
    if x == 100:
        print(cnt)
        break

    # 주사위 던지기 (1 ~ 6)
    for i in range(1, 7):
        nx = x + i

        if nx <= 100 and not visited[nx]:
            visited[nx] = True
            # 뱀이나 사다리가 있으면 이동, 없으면 그대로
            nx = ladder_snake.get(nx, nx)
            visited[nx] = True
            deq.append((nx, cnt + 1))
