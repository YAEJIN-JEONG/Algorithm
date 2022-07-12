# https://www.acmicpc.net/problem/17404
# RGB거리 2
from sys import stdin

n = int(stdin.readline())
cost = [list(map(int, stdin.readline().split())) for _ in range(n)]

answer = 1000 * n
# 첫번째 집을 i 색으로 고정
for i in range(3):
    dp = [[1000 * n] * 3 for _ in range(n)]
    dp[0][i] = cost[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + cost[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + cost[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + cost[j][2]

    # 마지막 집이 i 색이 아닌 경우만
    for j in range(3):
        if i == j:
            continue
        answer = min(answer, dp[-1][j])

print(answer)
