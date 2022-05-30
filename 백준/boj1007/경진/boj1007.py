# https://www.acmicpc.net/problem/1007
# 벡터 매칭
from sys import stdin
from itertools import combinations

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    answer = 1000000000

    # 점들의 좌표, x 좌표 합, y 좌표 합
    points, x_total, y_total = [], 0, 0
    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        points.append([x, y])
        x_total += x
        y_total += y

    # 시작점 절반 뽑는 조합
    for comb in combinations(range(N), N // 2):
        x_total_now, y_total_now = 0, 0
        for i in comb:
            x_total_now += points[i][0]
            y_total_now += points[i][1]

        # 뽑은 시작점 들의 좌표 빼기
        x_total_now = x_total - 2 * x_total_now
        y_total_now = y_total - 2 * y_total_now

        # 작은 값으로 갱신
        answer = min(answer, (x_total_now ** 2 + y_total_now ** 2) ** 0.5)

    print(answer)
