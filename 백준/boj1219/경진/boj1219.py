# https://www.acmicpc.net/problem/1219
# 오민식의 고민
from sys import stdin
from collections import deque


n, start, end, m = map(int, stdin.readline().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    edges[a].append([b, c])
values = list(map(int, stdin.readline().split()))

INF = 1 << 30
money = [-INF] * n
money[start] = values[start]

for cnt in range(n):
    for now in range(n):
        if money[now] == -INF:
            continue
        for to, cost in edges[now]:
            new_cost = money[now] - cost + values[to]

            if new_cost > money[to]:
                if cnt < n - 1:
                    money[to] = new_cost
                # cycle 생기는 경우
                else:
                    visited = [False] * n
                    visited[to] = True
                    deq = deque()
                    deq.append(to)

                    while deq:
                        v = deq.popleft()

                        if v == end:
                            print('Gee')
                            exit()

                        for v2, _ in edges[v]:
                            if not visited[v2]:
                                deq.append(v2)
                                visited[v2] = True

print('gg' if money[end] == -INF else money[end])
