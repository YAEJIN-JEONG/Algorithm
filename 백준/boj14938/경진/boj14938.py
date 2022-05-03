# https://www.acmicpc.net/problem/14938
# 서강그라운드
from sys import stdin

n, m, r = map(int, stdin.readline().split())
item_cnt = list(map(int, stdin.readline().split()))

INF = 1000000000
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = graph[b][a] = c

# 플로이드-와샬
for i in range(1, n + 1):
    # i 를 거쳤을 때 최단거리 갱신
    for fr in range(1, n + 1):
        for to in range(1, n + 1):
            graph[fr][to] = min(graph[fr][to], graph[fr][i] + graph[i][to])

answer = 0
# 자기 자신까지 거리 주의
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        if i == j or graph[i][j] <= m:
            total += item_cnt[j - 1]
    answer = max(answer, total)

print(answer)
