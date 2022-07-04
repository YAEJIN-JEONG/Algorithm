# https://www.acmicpc.net/problem/2162
# 선분 그룹
from sys import stdin
from collections import Counter

n = int(stdin.readline())
lines = [list(map(int, stdin.readline().split())) for _ in range(n)]
parent = [i for i in range(n)]


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def cross(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    d1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    d2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    if d1 == 0 and d2 == 0:
        return min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)
    else:
        return d1 <= 0 and d2 <= 0


# 분리 집합 (union - find)
def find(v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]


def union(a, b):
    pa, pb = find(a), find(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


for i in range(n):
    for j in range(i + 1, n):
        if cross(lines[i], lines[j]):
            union(i, j)

# 경로 압축 한번 더
for i in range(n):
    parent[i] = find(i)

counter = Counter(parent)
print(len(counter))
print(max(counter.values()))
