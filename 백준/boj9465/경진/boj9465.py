# https://www.acmicpc.net/problem/9465
# 스티커
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())

    score = [[i for i in map(int, stdin.readline().split())] for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    # 초기 세팅
    dp[0][0] = score[0][0]
    dp[1][0] = score[1][0]
    if n > 1:
        dp[0][1] = score[1][0] + score[0][1]
        dp[1][1] = score[0][0] + score[1][1]

    # 바로 이전 대각선과 그보다 더 이전 대각선 중에 더 큰 것 선택
    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + score[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + score[1][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))
