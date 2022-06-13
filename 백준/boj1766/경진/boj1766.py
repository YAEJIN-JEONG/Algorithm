# https://www.acmicpc.net/problem/1766
# 문제집
from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())

# 진입 차수, 진출 노드
in_degree, edges = [0] * (n + 1), [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    in_degree[b] += 1
    edges[a].append(b)

# 위상정렬 #

answer, q = [], []
# 진입 차수가 0인 노드 q 에 입력 (우선순위 큐)
for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    answer.append(now)

    for to in edges[now]:
        in_degree[to] -= 1

        # 진입 차수가 0이 되면 q 에 입력
        if in_degree[to] == 0:
            heapq.heappush(q, to)

print(*answer)
