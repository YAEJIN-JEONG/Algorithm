# https://www.acmicpc.net/problem/9251
# LCS
from sys import stdin

a, b = stdin.readline().rstrip(), stdin.readline().rstrip()
n, m = len(a) + 1, len(b) + 1

# 최장 공통 부분 수열 dp
dp = [[0] * m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n - 1][m - 1])
