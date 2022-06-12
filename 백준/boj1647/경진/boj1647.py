# https://www.acmicpc.net/problem/1647
# 도시 분할 계획
from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())

edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

# 최소 스패닝 트리 (prim)
q, connected, visited, total_cost, max_cost = [], 0, [False] * (n + 1), 0, 0
# 시작: 1번
heapq.heappush(q, (0, 1))

# 모든 정점 연결 시키기
while connected < n:
    cost, now = heapq.heappop(q)

    # now 가 연결되지 않았으면 연결
    if not visited[now]:
        total_cost += cost
        max_cost = max(max_cost, cost)
        connected += 1
        visited[now] = True

        for to, w in edges[now]:
            heapq.heappush(q, (w, to))

print(total_cost - max_cost)
