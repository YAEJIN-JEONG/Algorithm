# https://www.acmicpc.net/problem/16724
# 피리 부는 사나이
from sys import stdin

n, m = map(int, stdin.readline().split())
map_info = [stdin.readline().rstrip() for _ in range(n)]

parent = [[(r, c) for c in range(m)] for r in range(n)]


def find(pos):
    row, col = pos
    if parent[row][col] == (row, col):
        return row, col
    parent[row][col] = find(parent[row][col])
    return parent[row][col]


def union(pos1, pos2):
    row1, col1 = find(pos1)
    row2, col2 = find(pos2)

    if (row1, col1) < (row2, col2):
        parent[row2][col2] = (row1, col1)
    else:
        parent[row1][col1] = (row2, col2)


moves = {'D': (1, 0), 'L': (0, -1), 'U': (-1, 0), 'R': (0, 1)}
for x in range(n):
    for y in range(m):
        move = moves[map_info[x][y]]
        union((x, y), (x + move[0], y + move[1]))

safe_zone = set()
for x in range(n):
    for y in range(m):
        safe_zone.add(find((x, y)))

print(len(safe_zone))
