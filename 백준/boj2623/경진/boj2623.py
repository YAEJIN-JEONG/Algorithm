# https://www.acmicpc.net/problem/2623
# 음악프로그램
from sys import stdin

n, m = map(int, stdin.readline().split())
# 진입 차수, 진출 노드
in_degree = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    n_list = list(map(int, stdin.readline().split()[1:]))

    for i in range(len(n_list) - 1):
        edges[n_list[i]].append(n_list[i + 1])
        in_degree[n_list[i + 1]] += 1

v_list = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        v_list.append(i)

# 위상 정렬
cnt, answer = 0, []
while cnt < n and v_list:
    now = v_list.pop()
    answer.append(now)
    cnt += 1

    for to in edges[now]:
        in_degree[to] -= 1

        if in_degree[to] == 0:
            v_list.append(to)

print(0 if cnt < n else '\n'.join(map(str, answer)))
