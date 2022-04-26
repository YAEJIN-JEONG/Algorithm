# https://www.acmicpc.net/problem/11403
# 경로 찾기
from sys import stdin
from collections import deque

n = int(stdin.readline())
# 인접 행렬
matrix = [[i for i in map(int, stdin.readline().split())] for _ in range(n)]

# 모든 정점에 대해서 실행
for i in range(n):
    deq = deque()
    visited = [False] * n
    # 처음부터 연결되어있던 애들 큐에 집어넣고 초기 셋팅
    for j in range(n):
        if matrix[i][j] == 1 and not visited[j]:
            deq.append(j)
            visited[j] = True
    # bfs
    while deq:
        v = deq.popleft()
        # i -> v 경로가 있고, v -> k 경로가 있으면 i -> k 경로 존재
        for k in range(n):
            if matrix[v][k] == 1 and not visited[k]:
                matrix[i][k] = 1
                deq.append(k)
                visited[k] = True

for row in matrix:
    print(' '.join(map(str, row)))
