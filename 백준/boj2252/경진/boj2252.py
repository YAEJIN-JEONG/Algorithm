# https://www.acmicpc.net/problem/2252
# 줄 세우기
from sys import stdin

n, m = map(int, stdin.readline().split())

in_degree = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    edges[a].append(b)
    in_degree[b] += 1

# 위상 정렬
v_list = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        v_list.append(i)

cnt, answer = 0, []
while cnt < n:
    now = v_list.pop()
    answer.append(now)
    cnt += 1

    for to in edges[now]:
        in_degree[to] -= 1

        if in_degree[to] == 0:
            v_list.append(to)

print(' '.join(map(str, answer)))
