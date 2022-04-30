# https://www.acmicpc.net/problem/2606
from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())

# 인접 리스트
ad_list = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    ad_list[a].append(b)
    ad_list[b].append(a)

# bfs
dq = deque()
visited = [False for _ in range(n + 1)]
visited[1] = True
dq.append(1)
cnt = 0

while dq:
    v = dq.popleft()

    for i in ad_list[v]:
        if visited[i] == 0:
            dq.append(i)
            visited[i] = True
            cnt += 1

print(cnt)
