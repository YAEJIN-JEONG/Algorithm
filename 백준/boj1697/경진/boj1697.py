# https://www.acmicpc.net/problem/1697
from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
# 시작점 n 에서 시작하여 n-1, n+1, n*2 경우에 대해 bfs
dq = deque()
dq.append(n)
# 방문여부, 걸린시간 저장
visited = [0 for _ in range(100001)]

while dq:
    x = dq.popleft()

    if x == k:
        break

    nx_list = [x - 1, x + 1, x * 2]

    for nx in nx_list:
        if 0 <= nx <= 100000 and visited[nx] == 0:
            dq.append(nx)
            visited[nx] = visited[x] + 1

print(visited[k])
