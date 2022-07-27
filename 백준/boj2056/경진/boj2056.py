# https://www.acmicpc.net/problem/2056
# 작업
from sys import stdin

n = int(stdin.readline())
in_degree, edges = [0] * (n + 1), [[] for _ in range(n + 1)]
costs = [0] * (n + 1)

for i in range(n):
    s = list(map(int, stdin.readline().split()))
    costs[i + 1], in_degree[i + 1] = s[0], s[1]

    for node in s[2:]:
        edges[node].append(i + 1)

# 위상정렬
processing_nodes, time = set(), [0] * (n + 1)
for i in range(1, n + 1):
    if in_degree[i] == 0:
        time[i] = costs[i]
        processing_nodes.add(i)

answer = 0
while processing_nodes:
    now = processing_nodes.pop()

    for to in edges[now]:
        in_degree[to] -= 1
        time[to] = max(time[to], time[now] + costs[to])

        if in_degree[to] == 0:
            processing_nodes.add(to)

print(max(time))
