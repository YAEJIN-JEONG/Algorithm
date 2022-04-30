# https://www.acmicpc.net/problem/1389
from sys import stdin

n, m = map(int, stdin.readline().split())

INF = 1000000000
# 친구관계 그래프
friendship = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, stdin.readline().split())
    friendship[v1][v2] = friendship[v2][v1] = 1

# 플로이드-와샬 (모든 정점에서 다른 모든 정점까지의 최소비용 찾기)
for i in range(1, n + 1):
    # i 를 지날 때 최소비용 갱신
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            friendship[j][k] = min(friendship[j][k], friendship[j][i] + friendship[i][k])

# 케빈 베이컨의 수 가장 작은 사람 찾기
low = INF * n
index = 0
for i in range(1, n + 1):
    cost = sum(friendship[i])
    if low > cost:
        low = cost
        index = i

print(index)
