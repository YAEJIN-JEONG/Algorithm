# https://www.acmicpc.net/problem/4386
# 별자리 만들기
n = int(input())
star = [list(map(float, input().split())) for _ in range(n)]

edges, parent = [], [i for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        dist = ((star[i][0] - star[j][0]) ** 2 + (star[i][1] - star[j][1]) ** 2) ** 0.5
        edges.append([dist, i, j])

edges.sort(key=lambda x: x[0])


# 크루스칼 알고리즘
# cycle: union-find 로 확인
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
for dist, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        answer += dist

print(answer)
