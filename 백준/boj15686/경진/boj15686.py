# https://www.acmicpc.net/problem/15686
# 치킨 배달
from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())

# 집, 치킨집 위치 저장
house, chicken = [], []
for i in range(n):
    s = stdin.readline().rstrip().split()
    for j in range(n):
        if s[j] == '1':
            house.append((i, j))
        elif s[j] == '2':
            chicken.append((i, j))

# 각 집집마다 모든 치킨집까지의 거리 저장
# chicken_dist[i][j] 는 i번째 집에서 j번째 치킨집 까지의 거리
chicken_dist = [[abs(x1 - x2) + abs(y1 - y2) for x2, y2 in chicken] for x1, y1 in house]

combs = list(itertools.combinations([i for i in range(len(chicken))], m))

inf = 1000000000

answer = inf
# 모든 치킨집 조합에 대해 탐색
for comb in combs:
    # 치킨 거리의 합
    total = 0
    for i in range(len(house)):
        # i 번째 집의 치킨 거리
        dist = inf
        for c in comb:
            dist = min(dist, chicken_dist[i][c])
        total += dist
    answer = min(answer, total)

print(answer)
