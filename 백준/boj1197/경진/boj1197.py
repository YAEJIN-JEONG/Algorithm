# https://www.acmicpc.net/problem/1197
# 최소 스패닝 트리
from sys import stdin
import heapq

v, e = map(int, stdin.readline().split())
edges = [[] for _ in range(v + 1)]
for _ in range(e):
    fr, to, w = map(int, stdin.readline().split())
    edges[fr].append([to, w])
    edges[to].append([fr, w])

# prim algorithm #

answer, connected, q = 0, 0, []
visited = [False] * (v + 1)
# 시작점 1번 정점
heapq.heappush(q, (0, 1))

# 모든 정점이 연결될 때 까지
while connected < v:
    weight, now = heapq.heappop(q)

    # now 가 아직 연결 상태가 아니면 연결
    if not visited[now]:
        answer += weight
        connected += 1
        visited[now] = True

        for to, w in edges[now]:
            heapq.heappush(q, (w, to))

print(answer)
