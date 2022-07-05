# https://www.acmicpc.net/problem/2887
# 행성 터널
from sys import stdin

n = int(stdin.readline())
points = [list(map(int, stdin.readline().split())) + [i] for i in range(n)]

edges, parent = [], [i for i in range(n)]
# x, y, z 별로 정렬한 뒤, 가장 거리가 짧은 거 우선 선택
for k in range(3):
    points.sort(key=lambda x: x[k])
    for i in range(n - 1):
        edges.append([abs(points[i][k] - points[i + 1][k]), points[i][3], points[i + 1][3]])

edges.sort(key=lambda x: x[0])


# 크루스칼 알고리즘
# cycle: union-find 로 검증
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px, py = find(x), find(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py


answer = 0
for d, i, j in edges:
    if find(i) != find(j):
        answer += d
        union(i, j)

print(answer)
