# https://www.acmicpc.net/problem/9461
# 파도반 수열
# dp 문제, 규칙 찾기
from sys import stdin

t = int(stdin.readline())

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(t):
    n = int(stdin.readline())

    # 점화식: f(n) = f(n - 2) + f(n - 3),  (n >= 6)
    for i in range(len(dp), n + 1):
        dp.append(dp[i - 2] + dp[i - 3])

    print(dp[n])
