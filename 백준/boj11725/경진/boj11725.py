# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기
from sys import stdin
from collections import deque

n = int(stdin.readline())
edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

# 부모 노드 번호 저장
parent = [0 for _ in range(n + 1)]

# bfs
deq = deque()
deq.append(1)
parent[1] = 1

while deq:
    v1 = deq.popleft()
    # v1 과 연결된 노드 탐색
    for v2 in edges[v1]:
        # 부모 노드 번호가 0이면 아직 방문x
        if parent[v2] == 0:
            deq.append(v2)
            parent[v2] = v1

for i in range(2, n + 1):
    print(parent[i])
