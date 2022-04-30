# https://www.acmicpc.net/problem/1149
# RGB 거리
from sys import stdin

n = int(stdin.readline())
cost = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0, 0, 0]]
# 칠할 색 선택하는 방법 중 cost 가 더 적은 경우 선택해서 저장
for i in range(1, n + 1):
    i_cost = [
        min(dp[i - 1][1], dp[i - 1][2]) + cost[i - 1][0],
        min(dp[i - 1][0], dp[i - 1][2]) + cost[i - 1][1],
        min(dp[i - 1][0], dp[i - 1][1]) + cost[i - 1][2]
    ]
    dp.append(i_cost)

print(min(dp[n]))
