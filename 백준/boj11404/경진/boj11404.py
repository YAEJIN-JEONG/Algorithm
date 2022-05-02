# https://www.acmicpc.net/problem/11404
# 플로이드
from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

inf = 1000000000
graph = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

# 플로이드-와샬
for i in range(1, n + 1):
    # i 를 지나서 가는 경우 갱신
    for x in range(1, n + 1):
        # x -> y, x -> i -> y 중에 더 비용이 적은 것 선택
        for y in range(1, n + 1):
            graph[x][y] = min(graph[x][y], graph[x][i] + graph[i][y])

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print(0, end=' ')
        else:
            print(graph[i][j] % inf, end=' ')
    print()
